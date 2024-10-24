import openpyxl
import csv
import io


class ExcelConverter:
    def transform(self, data):
        return [
            {
                "original": item["original"],
                "filename": f"{item['basename']}.xlsx",
                "content": item["content"],
                "xlsxContent": self.convert_to_excel_like(
                    item["content"], "xlsx"
                ),
                "csvContent": self.convert_to_excel_like(
                    item["content"], "csv"
                ),
            }
            for item in data
        ]

    def convert_to_excel_like(self, content, book_type):
        separator, preprocessed_content = self.preprocess_content(content)

        if book_type == "xlsx":
            wb = openpyxl.Workbook()
            ws = wb.active
            for row in csv.reader(
                io.StringIO(preprocessed_content), delimiter=separator
            ):
                ws.append(row)

            output = io.BytesIO()
            wb.save(output)
            return output.getvalue()
        elif book_type == "csv":
            return preprocessed_content.encode("utf-8")

    def preprocess_content(self, content):
        options = self.options(content)
        preprocessed_content = "\n".join(
            content.split("\n")[options["lines_to_skip"] :]
        )

        if options["must_merge_separators"]:
            preprocessed_content = preprocessed_content.replace(
                f"{options['separator']}{options['separator']}",
                options["separator"],
            )
            preprocessed_content = preprocessed_content.replace(
                f"\n{options['separator']}", "\n"
            )

        return options["separator"], preprocessed_content

    def options(self, content):
        if "[Data]" in content:
            return {
                "separator": ",",
                "must_merge_separators": False,
                "lines_to_skip": 30,
            }
        return {
            "separator": " ",
            "must_merge_separators": True,
            "lines_to_skip": 2,
        }
