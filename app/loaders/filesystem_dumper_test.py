import unittest
from pathlib import Path

from ..core import Records
from .filesystem_dumper import FilesystemDumper

OUTPUT_FOLDER = Path("./output")


class TestFilesystemDumper(unittest.TestCase):
    def setUp(self) -> None:
        self.instance = FilesystemDumper()
        self.file_path = OUTPUT_FOLDER / "file_dumper_test.txt"
        self.content = b"Some content"
        OUTPUT_FOLDER.mkdir(exist_ok=True)

    def test_load_writes_content_to_output_folder(self) -> None:
        self.instance.load(
            Records(
                records=[
                    {
                        "filename": self.file_path.name,
                        "content": self.content,
                    }
                ]
            )
        )
        written_data = self.file_path.read_bytes()
        self.assertEqual(written_data, self.content)

    def tearDown(self) -> None:
        if self.file_path.exists():
            self.file_path.unlink()


if __name__ == "__main__":
    unittest.main()
