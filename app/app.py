"""
Main entry point for the ETL pipeline application.

This module initializes and runs the ETL (Extract, Transform, Load) pipeline
with the configured components for data extraction, transformation, and loading.
"""

from .extractors.data_extractor import DataExtractor
from .loaders.filesystem_dumper import FilesystemDumper
from .pipelines.etl_pipeline import ETLPipeline
from .transformers.excel_converter import ExcelConverter


def main() -> None:
    """Run the ETL pipeline."""
    pipeline = ETLPipeline(
        extractor=DataExtractor(),
        transformer=ExcelConverter(),
        loader=FilesystemDumper(),
    )
    pipeline.perform()


if __name__ == "__main__":
    main()
