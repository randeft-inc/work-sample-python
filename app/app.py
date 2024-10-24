from pipelines.ETLPipeline import ETLPipeline
from extractors.DataExtractor import DataExtractor
from transformers.ExcelConverter import ExcelConverter
from loaders.FilesystemDumper import FilesystemDumper


if __name__ == "__main__":

    extractor = DataExtractor()
    transformer = ExcelConverter()
    loader = FilesystemDumper()

    pipeline = ETLPipeline(
        extractor=extractor, transformer=transformer, loader=loader
    )

    pipeline.perform()
