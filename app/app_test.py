import unittest
from unittest.mock import MagicMock, patch


class TestApp(unittest.TestCase):
    @patch("app.app.ETLPipeline")
    @patch("app.app.DataExtractor")
    @patch("app.app.ExcelConverter")
    @patch("app.app.FilesystemDumper")
    def test_main_flow(
        self,
        mock_loader: MagicMock,
        mock_transformer: MagicMock,
        mock_extractor: MagicMock,
        mock_pipeline: MagicMock,
    ) -> None:
        # Create mock instances
        mock_pipeline_instance = MagicMock()
        mock_extractor_instance = MagicMock()
        mock_transformer_instance = MagicMock()
        mock_loader_instance = MagicMock()

        # Configure mocks
        mock_pipeline.return_value = mock_pipeline_instance
        mock_extractor.return_value = mock_extractor_instance
        mock_transformer.return_value = mock_transformer_instance
        mock_loader.return_value = mock_loader_instance

        # Run the main function
        from app.app import main

        main()

        # Verify pipeline was created with correct components
        mock_pipeline.assert_called_once_with(
            extractor=mock_extractor_instance,
            transformer=mock_transformer_instance,
            loader=mock_loader_instance,
        )

        # Verify pipeline was executed
        mock_pipeline_instance.perform.assert_called_once()


if __name__ == "__main__":
    unittest.main()
