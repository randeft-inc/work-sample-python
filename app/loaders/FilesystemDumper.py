from pathlib import Path
from typing import List
from ..data_types import TransformedData

OUTPUT_FOLDER = Path("./output")


class FilesystemDumper:
    """Loader implementation that writes data to files in a local output folder."""

    def load(self, data: List[TransformedData]) -> None:
        OUTPUT_FOLDER.mkdir(exist_ok=True)
        for item in data:
            filepath = OUTPUT_FOLDER / item["filename"]
            filepath.write_bytes(item["content"])
