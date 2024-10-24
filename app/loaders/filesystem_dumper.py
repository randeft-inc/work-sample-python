from pathlib import Path

from ..core import Records

OUTPUT_FOLDER = Path("./output")


class FilesystemDumper:
    """Loader implementation that writes data to files in a local output folder."""

    def load(self, data: Records) -> None:
        """Dump the transformed data to the output folder."""
        OUTPUT_FOLDER.mkdir(exist_ok=True)
        for item in data:
            filepath = OUTPUT_FOLDER / item["filename"]
            filepath.write_bytes(item["content"])
