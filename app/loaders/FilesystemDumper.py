import os

OUTPUT_FOLDER = "./output"


class FilesystemDumper:
    def load(self, data):
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)
        for item in data:
            filename = item["filename"]
            content = item["content"]
            filepath = os.path.join(OUTPUT_FOLDER, filename)
            with open(filepath, "wb") as file:
                # Convert content to bytes if it's a string
                if isinstance(content, str):
                    content = content.encode("utf-8")
                file.write(content)
