from typing import Protocol, List
from ..data_types import ExtractedData, TransformedData


class Extractor(Protocol):
    def extract(self) -> List[ExtractedData]: ...


class Transformer(Protocol):
    def transform(self, data: List[ExtractedData]) -> List[TransformedData]: ...


class Loader(Protocol):
    def load(self, data: List[TransformedData]) -> None: ...


class ETLPipeline:
    """Main ETL pipeline that orchestrates the extract, transform, and load process."""

    def __init__(
        self,
        extractor: Extractor,
        transformer: Transformer,
        loader: Loader,
    ) -> None:
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader

    def perform(self) -> None:
        extracted_data = self.extractor.extract()
        transformed_data = self.transformer.transform(extracted_data)
        self.loader.load(transformed_data)
