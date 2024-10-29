from pathlib import Path
from typing import List
from ..data_types import ExtractedData

INPUT_FOLDER = Path("./raw_data/")


class DataExtractor:
    """Extracts data from raw data files.

    For this sample, the extractor reads files from the local disk.
    In practice, it would get data from an external system.
    """

    def extract(self) -> List[ExtractedData]:
        filenames = sorted(INPUT_FOLDER.iterdir())
        return [
            {
                "basename": filename.stem,
                "content": filename.read_text(encoding="utf-8"),
            }
            for filename in filenames
        ]
