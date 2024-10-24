from typing import Protocol

from ..core import Records


class Extractor(Protocol):
    """Protocol for data extraction."""

    def extract(self) -> Records:
        """Extract the data from the source system."""
        ...


class Transformer(Protocol):
    """Protocol for data transformation."""

    def transform(self, data: Records) -> Records:
        """Transform the input data."""
        ...


class Loader(Protocol):
    """Protocol for data loading."""

    def load(self, data: Records) -> None:
        """Load the transformed data into the target system."""
        ...


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
        """Perform the ETL pipeline."""
        extracted_data = self.extractor.extract()
        transformed_data = self.transformer.transform(extracted_data)
        self.loader.load(transformed_data)
