import unittest
from .ExcelConverter import ExcelConverter


class TestExcelConverter(unittest.TestCase):
    def setUp(self):
        self.instance = ExcelConverter({})

    def test_transform_type_1_data(self):
        basename = "type_1"
        with open("./raw_data/sample_1.dat", "r", encoding="utf-8") as f:
            content = f.read()

        transformed = self.instance.transform(
            [{"basename": basename, "content": content}]
        )

        self.assertEqual(transformed[0]["filename"], "type_1.xlsx")
        # for simplicity we only verify the content length
        self.assertEqual(len(transformed[0]["content"]), 151141)

    def test_transform_type_2_data(self):
        basename = "type_2"
        with open("./raw_data/sample_2.dat", "r", encoding="utf-8") as f:
            content = f.read()

        transformed = self.instance.transform(
            [{"basename": basename, "content": content}]
        )

        self.assertEqual(transformed[0]["filename"], "type_2.xlsx")
        # for simplicity we only verify the content length
        self.assertEqual(len(transformed[0]["content"]), 84105)


if __name__ == "__main__":
    unittest.main()
