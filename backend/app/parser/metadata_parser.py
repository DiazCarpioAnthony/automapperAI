import re

from app.models.metadata import Metadata


class MetadataParser:

    def _get_tag(self, text: str, tag: str, default=""):
        pattern = rf"#{tag}:(.*?);"
        match = re.search(pattern, text, re.DOTALL)

        if match:
            return match.group(1).strip()

        return default

    def parse(self, text: str) -> Metadata:

        return Metadata(

            title=self._get_tag(text, "TITLE"),

            subtitle=self._get_tag(text, "SUBTITLE"),

            artist=self._get_tag(text, "ARTIST"),

            title_translit=self._get_tag(text, "TITLETRANSLIT"),

            subtitle_translit=self._get_tag(text, "SUBTITLETRANSLIT"),

            artist_translit=self._get_tag(text, "ARTISTTRANSLIT"),

            credit=self._get_tag(text, "CREDIT"),

            banner=self._get_tag(text, "BANNER"),

            background=self._get_tag(text, "BACKGROUND"),

            cd_title=self._get_tag(text, "CDTITLE"),

            lyrics_path=self._get_tag(text, "LYRICSPATH"),

            music=self._get_tag(text, "MUSIC"),

            offset=float(self._get_tag(text, "OFFSET", 0)),

            sample_start=float(self._get_tag(text, "SAMPLESTART", 0)),

            sample_length=float(self._get_tag(text, "SAMPLELENGTH", 0)),

            selectable=self._get_tag(text, "SELECTABLE", "YES") == "YES",
        )