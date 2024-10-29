"""Main entry point for the ETL pipeline application.

This module initializes and runs the ETL (Extract, Transform, Load) pipeline
with the configured components for data extraction, transformation, and loading.
"""

from .pipelines.ETLPipeline import ETLPipeline
from .extractors.DataExtractor import DataExtractor
from .transformers.ExcelConverter import ExcelConverter
from .loaders.FilesystemDumper import FilesystemDumper

if __name__ == "__main__":
    pipeline = ETLPipeline(
        extractor=DataExtractor(),
        transformer=ExcelConverter(),
        loader=FilesystemDumper(),
    )

    pipeline.perform()
