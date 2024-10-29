from openpyxl import Workbook
from io import BytesIO, StringIO
from csv import reader
from typing import List, Dict, Tuple, Union
from ..data_types import ExtractedData, TransformedData


class ExcelConverter:
    """Transforms input data into Excel (XLSX) format."""

    def transform(self, data: List[ExtractedData]) -> List[TransformedData]:
        return [
            {
                "filename": f"{item['basename']}.xlsx",
                "content": self._convert_to_excel(item["content"]),
            }
            for item in data
        ]

    def _convert_to_excel(self, content: str) -> bytes:
        separator, preprocessed_content = self._preprocess_content(content)
        workbook = self._xlsx_read(preprocessed_content, separator)
        return self._xlsx_write(workbook)

    def _xlsx_read(self, preprocessed_content: str, separator: str) -> Workbook:
        workbook = Workbook()
        for row in reader(StringIO(preprocessed_content), delimiter=separator):
            workbook.active.append(row)
        return workbook

    def _xlsx_write(self, workbook: Workbook) -> bytes:
        buffer = BytesIO()
        workbook.save(buffer)
        return buffer.getvalue()

    def _preprocess_content(self, content: str) -> Tuple[str, str]:
        options = self._options(content)
        separator = options["separator"]
        processed = "\n".join(content.split("\n")[options["lines_to_skip"] :])
        if options["must_merge_separators"]:
            processed = self._merge_separators(processed, separator)
        return separator, processed

    def _merge_separators(self, content: str, separator: str) -> str:
        return content.replace(
            f"{separator}{separator}",
            separator,
        ).replace(
            f"\n{separator}",
            "\n",
        )

    def _options(self, content: str) -> Dict[str, Union[str, bool, int]]:
        # Simplistic heuristic to classify two types of files
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
