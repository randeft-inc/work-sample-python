import unittest
from pathlib import Path
from .ExcelConverter import ExcelConverter


class TestTransformType1Data(unittest.TestCase):
    def setUp(self):
        basename = "type_1"
        content = Path("./raw_data/sample_1.dat").read_text(encoding="utf-8")
        self.transformed = ExcelConverter().transform(
            [{"basename": basename, "content": content}]
        )

    def test_generates_expected_filename(self):
        self.assertEqual(self.transformed[0]["filename"], "type_1.xlsx")

    def test_generates_expected_content(self):
        # For simplicity we only verify the content length. It is changing due to
        # random metadata like creation time.
        content_length = len(self.transformed[0]["content"])
        self.assertTrue(
            59708 <= content_length <= 59712,
            f"Content length {content_length} outside expected range",
        )


class TestTransformType2Data(unittest.TestCase):
    def setUp(self):
        basename = "type_2"
        content = Path("./raw_data/sample_2.dat").read_text(encoding="utf-8")
        self.transformed = ExcelConverter().transform(
            [{"basename": basename, "content": content}]
        )

    def test_generates_expected_filename(self):
        self.assertEqual(self.transformed[0]["filename"], "type_2.xlsx")

    def test_generates_expected_content(self):
        # For simplicity we only verify the content length. It is changing due to
        # random metadata like creation time.
        content_length = len(self.transformed[0]["content"])
        self.assertTrue(
            25428 <= content_length <= 25433,
            f"Content length {content_length} outside expected range",
        )


if __name__ == "__main__":
    unittest.main()
