import unittest
from unittest.mock import Mock
from .ETLPipeline import ETLPipeline


class TestETLPipeline(unittest.TestCase):
    def setUp(self):
        self.extract = Mock(return_value="extracted")
        self.transform = Mock(return_value="transformed")
        self.load = Mock()

        extractor = Mock()
        extractor.extract = self.extract

        transformer = Mock()
        transformer.transform = self.transform

        loader = Mock()
        loader.load = self.load

        self.instance = ETLPipeline(
            extractor=extractor,
            transformer=transformer,
            loader=loader,
        )

    def test_perform(self):
        # Verify initial state
        self.extract.assert_not_called()
        self.transform.assert_not_called()
        self.load.assert_not_called()

        # Perform the ETL process
        self.instance.perform()

        # Test that extract is called on the extractor
        self.extract.assert_called_once()

        # Test that transform is called on the transformer
        self.transform.assert_called_once()

        # Test that load is called on the loader
        self.load.assert_called_once()

        # Test that extracted data is passed to the transformer
        self.transform.assert_called_with("extracted")

        # Test that transformed data is passed to the loader
        self.load.assert_called_with("transformed")


if __name__ == "__main__":
    unittest.main()
