import unittest
import os
import shutil
from .FilesystemDumper import FilesystemDumper

OUTPUT_FOLDER = "./output"


class TestFilesystemDumper(unittest.TestCase):
    def setUp(self):
        self.instance = FilesystemDumper()
        self.file_path = os.path.join(OUTPUT_FOLDER, "file_dumper_test.txt")
        self.content = "Some content"
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    def test_load_writes_content_to_output_folder(self):
        self.instance.load(
            [
                {
                    "filename": os.path.basename(self.file_path),
                    "content": self.content,
                },
            ]
        )

        with open(self.file_path, "r", encoding="utf-8") as file:
            written_data = file.read()

        self.assertEqual(written_data, self.content)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)


if __name__ == "__main__":
    unittest.main()
