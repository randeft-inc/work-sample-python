import unittest
from unittest.mock import Mock
from .ETLPipeline import ETLPipeline


class TestETLPipeline(unittest.TestCase):
    def setUp(self):
        extractor = Mock()
        transformer = Mock()
        loader = Mock()

        extractor.extract = self.extract = Mock(return_value="extracted")
        transformer.transform = self.transform = Mock(return_value="transformed")
        loader.load = self.load = Mock()

        self.instance = ETLPipeline(
            extractor=extractor,
            transformer=transformer,
            loader=loader,
        )
        self.extract.assert_not_called()
        self.transform.assert_not_called()
        self.load.assert_not_called()

        self.instance.perform()

    def test_calls_extract_on_extractor(self):
        self.extract.assert_called_once()

    def test_calls_transform_on_transformer(self):
        self.transform.assert_called_once()

    def test_calls_load_on_loader(self):
        self.load.assert_called_once()

    def test_passes_extracted_data_to_transformer(self):
        self.transform.assert_called_with("extracted")

    def test_passes_transformed_data_to_loader(self):
        self.load.assert_called_with("transformed")


if __name__ == "__main__":
    unittest.main()
