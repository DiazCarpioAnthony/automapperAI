import re

from app.models.measure import Measure
from app.parser.chart_header_parser import ChartHeaderParser


class MeasureParser:

    NOTE_ROW_PATTERN = ChartHeaderParser.NOTE_ROW_PATTERN

    def parse(self, body: str) -> list[Measure]:
        """
        Divide el cuerpo de un bloque #NOTES: en compases.
        Cada compás se separa por comas (,).
        """

        measures: list[Measure] = []
        current_rows: list[str] = []

        for raw_line in body.splitlines():
            cleaned = self._clean_line(raw_line)

            if not cleaned:
                continue

            if self._is_measure_separator(cleaned):
                self._close_measure(measures, current_rows)
                current_rows = []
                continue

            row, has_trailing_comma = self._extract_row(cleaned)

            if row is None:
                raise ValueError(
                    f"Línea de notas inválida en chart: {raw_line!r}"
                )

            current_rows.append(row)

            if has_trailing_comma:
                self._close_measure(measures, current_rows)
                current_rows = []

        if current_rows:
            measures.append(Measure(rows=current_rows))

        if not measures:
            raise ValueError("El cuerpo del chart no contiene compases")

        return measures

    def _clean_line(self, line: str) -> str:
        if "//" in line:
            line = line.split("//", 1)[0]

        return line.strip()

    def _is_measure_separator(self, cleaned: str) -> bool:
        return cleaned == ","

    def _extract_row(self, cleaned: str) -> tuple[str | None, bool]:
        has_trailing_comma = cleaned.endswith(",")

        if has_trailing_comma:
            cleaned = cleaned[:-1].strip()

        if not cleaned:
            return None, has_trailing_comma

        if not self.NOTE_ROW_PATTERN.match(cleaned):
            return None, has_trailing_comma

        return cleaned, has_trailing_comma

    def _close_measure(
        self,
        measures: list[Measure],
        current_rows: list[str],
    ) -> None:
        if not current_rows:
            return

        measures.append(Measure(rows=list(current_rows)))
