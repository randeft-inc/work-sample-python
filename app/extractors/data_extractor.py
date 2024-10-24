from pathlib import Path

from ..core import Records

INPUT_FOLDER = Path("./raw_data/")


class DataExtractor:
    """
    Extracts data from raw data files.

    For this sample, the extractor reads files from the local disk.
    In practice, it would get data from an external system.
    """

    def extract(self) -> Records:
        """Extract the data from the source system."""
        filenames = sorted(INPUT_FOLDER.iterdir())
        return Records(
            records=[
                {
                    "basename": filename.stem,
                    "content": filename.read_text(encoding="utf-8"),
                }
                for filename in filenames
            ]
        )
