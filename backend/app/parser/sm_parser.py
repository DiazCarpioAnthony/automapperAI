from pathlib import Path

from app.models.song import Song
from app.parser.metadata_parser import MetadataParser
from app.parser.timing_parser import TimingParser
from app.parser.chart_parser import ChartParser


class SMParser:

    def __init__(self):

        self.metadata_parser = MetadataParser()
        self.timing_parser = TimingParser()
        self.chart_parser = ChartParser()

    def parse(self, path):

        text = Path(path).read_text(
            encoding="utf-8",
            errors="replace"
        )

        metadata = self.metadata_parser.parse(text)
        timing = self.timing_parser.parse(text)
        charts = self.chart_parser.parse(text)

        song = Song(
            metadata=metadata,
            timing=timing,
            charts=charts
        )

        return song