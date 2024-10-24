from csv import reader
from datetime import datetime
from io import BytesIO, StringIO
from typing import Dict, List, Tuple, Union

import xlsxwriter

from ..core import Records


class ExcelConverter:
    """Transforms input data into Excel (XLSX) format."""

    def transform(self, data: Records) -> Records:
        """Transform the input data into Excel (XLSX) format."""
        return Records(
            records=[
                {
                    "filename": f"{item['basename']}.xlsx",
                    "content": self._convert_to_excel(item["content"]),
                }
                for item in data
            ]
        )

    def _convert_to_excel(self, content: str) -> bytes:
        """Convert the input data into Excel (XLSX) format."""
        separator, preprocessed_content = self._preprocess_content(content)
        rows = self._read_csv(preprocessed_content, separator)
        return self._write_xlsx(rows)

    def _read_csv(self, preprocessed_content: str, separator: str) -> List[List[str]]:
        """Read CSV content into a list of rows."""
        return list(reader(StringIO(preprocessed_content), delimiter=separator))

    def _write_xlsx(self, rows: List[List[str]]) -> bytes:
        """Write rows to an XLSX file using xlsxwriter."""
        buffer = BytesIO()
        workbook = xlsxwriter.Workbook(buffer, {"in_memory": True})
        worksheet = workbook.add_worksheet()
        for row_idx, row in enumerate(rows):
            for col_idx, value in enumerate(row):
                worksheet.write(row_idx, col_idx, value)
        timestamp = datetime(2000, 1, 1, 0, 0, 0)
        workbook.set_properties({"created": timestamp, "modified": timestamp})
        workbook.close()
        return buffer.getvalue()

    def _preprocess_content(self, content: str) -> Tuple[str, str]:
        options = self._options(content)
        separator = str(options["separator"])
        processed = "\n".join(content.split("\n")[int(options["lines_to_skip"]) :])
        if options["must_merge_separators"]:
            processed = self._merge_separators(processed, separator)
        return separator, processed

    def _merge_separators(self, content: str, separator: str) -> str:
        """Merge separators in the input data."""
        return content.replace(
            f"{separator}{separator}",
            separator,
        ).replace(
            f"\n{separator}",
            "\n",
        )

    def _options(self, content: str) -> Dict[str, Union[str, bool, int]]:
        """Determine the options for the input data."""
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
