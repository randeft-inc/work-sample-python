import unittest
from unittest.mock import Mock

from ..core import Records
from .etl_pipeline import ETLPipeline


class TestETLPipeline(unittest.TestCase):
    def setUp(self) -> None:
        extractor = Mock()
        transformer = Mock()
        loader = Mock()

        extracted = Records(records=[{"content": "extracted"}])
        transformed = Records(records=[{"content": "transformed"}])

        extractor.extract = self.extract = Mock(return_value=extracted)
        transformer.transform = self.transform = Mock(return_value=transformed)
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

    def test_calls_extract_on_extractor(self) -> None:
        self.extract.assert_called_once()

    def test_calls_transform_on_transformer(self) -> None:
        self.transform.assert_called_once()

    def test_calls_load_on_loader(self) -> None:
        self.load.assert_called_once()

    def test_passes_extracted_data_to_transformer(self) -> None:
        self.transform.assert_called_with(self.extract.return_value)

    def test_passes_transformed_data_to_loader(self) -> None:
        self.load.assert_called_with(self.transform.return_value)


if __name__ == "__main__":
    unittest.main()
