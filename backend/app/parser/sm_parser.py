from pathlib import Path

from app.parser.metadata_parser import MetadataParser


class SMParser:

    def __init__(self):

        self.metadata_parser = MetadataParser()

    def parse(self, path):

        text = Path(path).read_text(
            encoding="utf-8",
            errors="replace"
        )

        metadata = self.metadata_parser.parse(text)

        print(metadata)