import os

INPUT_FOLDER = "./raw_data/"


class DataExtractor:
    def extract(self):
        filenames = sorted(os.listdir(INPUT_FOLDER))
        return [
            {
                "original": filename,
                "basename": os.path.splitext(filename)[0],
                "content": self._read_file(
                    os.path.join(INPUT_FOLDER, filename)
                ),
            }
            for filename in filenames
        ]

    def _read_file(self, file_path):
        with open(file_path, "r") as file:
            return file.read()
