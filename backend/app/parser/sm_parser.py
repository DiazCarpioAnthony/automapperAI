from pathlib import Path


class SMParser:

    def parse(self, path: str):

        text = Path(path).read_text(
            encoding="utf-8",
            errors="replace"
        )

        print(text[:500])