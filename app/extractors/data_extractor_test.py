import unittest

from .data_extractor import DataExtractor


class TestDataExtractor(unittest.TestCase):
    def setUp(self) -> None:
        self.instance = DataExtractor()
        self.subject = self.instance.extract()

    def test_returns_2_items(self) -> None:
        items_count = len(self.subject)
        self.assertEqual(items_count, 2)

    def test_items_have_expected_basenames(self) -> None:
        basenames = [data["basename"] for data in self.subject]
        self.assertEqual(basenames, ["sample_1", "sample_2"])

    def test_items_have_expected_contents(self) -> None:
        excerpts = [data["content"][:8] for data in self.subject]
        self.assertEqual(excerpts, ["2006/12/", "[Header]"])


if __name__ == "__main__":
    unittest.main()
