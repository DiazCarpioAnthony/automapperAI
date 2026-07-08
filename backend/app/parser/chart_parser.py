import re

from app.models.chart import Chart
from app.parser.chart_header_parser import ChartHeaderParser
from app.parser.measure_parser import MeasureParser


class ChartParser:

    def __init__(self):
        self.header_parser = ChartHeaderParser()
        self.measure_parser = MeasureParser()

    def parse(self, text: str) -> list[Chart]:
        charts = []

        for block in self._extract_blocks(text):
            chart, body = self.header_parser.split(block)
            chart.measures = self.measure_parser.parse(body)
            charts.append(chart)

        return charts

    def _extract_blocks(self, text: str) -> list[str]:
        pattern = r"#NOTES:(.*?);"

        matches = re.findall(
            pattern,
            text,
            re.DOTALL,
        )

        return [match.strip() for match in matches]
