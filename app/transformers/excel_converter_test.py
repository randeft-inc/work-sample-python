import hashlib
import unittest
from pathlib import Path

from ..core import Records
from .excel_converter import ExcelConverter


class TestTransformType1Data(unittest.TestCase):
    def setUp(self) -> None:
        basename = "type_1"
        content = Path("./raw_data/sample_1.dat").read_text(encoding="utf-8")
        self.transformed = ExcelConverter().transform(
            Records(records=[{"basename": basename, "content": content}])
        )

    def test_generates_expected_filename(self) -> None:
        self.assertEqual(self.transformed[0]["filename"], "type_1.xlsx")

    def test_generates_expected_content(self) -> None:
        content_hash = hashlib.sha256(self.transformed[0]["content"]).hexdigest()
        self.assertEqual(
            content_hash,
            "1e1ff7c0062329447a5e957182ba085b294d2894716cdf6949f6eb3ce87f357d",
        )


class TestTransformType2Data(unittest.TestCase):
    def setUp(self) -> None:
        basename = "type_2"
        content = Path("./raw_data/sample_2.dat").read_text(encoding="utf-8")
        self.transformed = ExcelConverter().transform(
            Records(records=[{"basename": basename, "content": content}])
        )

    def test_generates_expected_filename(self) -> None:
        self.assertEqual(self.transformed[0]["filename"], "type_2.xlsx")

    def test_generates_expected_content(self) -> None:
        content_hash = hashlib.sha256(self.transformed[0]["content"]).hexdigest()
        self.assertEqual(
            content_hash,
            "41f834535919fbf2d15fc576f7c88bf61d40d20a5fe37feb88f1fbdf6636cb46",
        )


if __name__ == "__main__":
    unittest.main()
