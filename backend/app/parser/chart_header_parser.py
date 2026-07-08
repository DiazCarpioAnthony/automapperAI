import re

from app.core.enums import Difficulty
from app.models.chart import Chart


class ChartHeaderParser:

    STEP_TYPE_PATTERN = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)+$")
    METER_PATTERN = re.compile(r"^\d+$")
    RADAR_PATTERN = re.compile(r"^[-\d.]+(?:\s*,\s*[-\d.]+)+$")
    NOTE_ROW_PATTERN = re.compile(r"^[0-4MRLFK]{4,8}$")

    def parse(self, block: str) -> Chart:
        chart, _body = self.split(block)
        return chart

    def split(self, block: str) -> tuple[Chart, str]:
        """
        Valida y parsea la cabecera de un bloque #NOTES:.
        Devuelve el Chart y el texto restante (cuerpo de notas).
        """

        lines = self._non_empty_lines(block)

        if len(lines) < 5:
            raise ValueError(
                "Cabecera #NOTES: incompleta: se esperaban al menos 5 líneas "
                f"con contenido, se encontraron {len(lines)}"
            )

        index = 0
        step_type, index = self._read_step_type(lines, index)
        description, index = self._read_description(lines, index)
        difficulty, index = self._read_difficulty(lines, index)
        meter, index = self._read_meter(lines, index)
        radar, index = self._read_radar(lines, index)

        body = "\n".join(line for line, _ in lines[index:])

        chart = Chart(
            step_type=step_type,
            description=description,
            difficulty=difficulty,
            meter=meter,
            radar=radar,
        )

        return chart, body

    def _non_empty_lines(self, block: str) -> list[tuple[str, str]]:
        result = []

        for line in block.splitlines():
            cleaned = self._clean_line(line)

            if cleaned:
                result.append((line, cleaned))

        return result

    def _clean_line(self, line: str) -> str:
        if "//" in line:
            line = line.split("//", 1)[0]

        return line.strip()

    def _value_before_colon(self, cleaned: str) -> str:
        if not cleaned.endswith(":"):
            raise ValueError(
                f"Línea de cabecera inválida (falta ':' final): {cleaned!r}"
            )

        return cleaned[:-1].strip()

    def _read_step_type(
        self,
        lines: list[tuple[str, str]],
        index: int,
    ) -> tuple[str, int]:
        raw, cleaned = lines[index]
        value = self._value_before_colon(cleaned)

        if not value:
            raise ValueError(
                f"Línea 1 de cabecera inválida: step_type vacío en {raw!r}"
            )

        if not self.STEP_TYPE_PATTERN.match(value):
            raise ValueError(
                f"Línea 1 de cabecera inválida: step_type no reconocido {value!r} "
                f"(se espera formato tipo 'dance-single')"
            )

        return value, index + 1

    def _read_description(
        self,
        lines: list[tuple[str, str]],
        index: int,
    ) -> tuple[str, int]:
        _raw, cleaned = lines[index]

        try:
            value = self._value_before_colon(cleaned)
        except ValueError as error:
            raise ValueError(
                f"Línea 2 de cabecera inválida: description mal formada: {error}"
            ) from error

        return value, index + 1

    def _read_difficulty(
        self,
        lines: list[tuple[str, str]],
        index: int,
    ) -> tuple[Difficulty, int]:
        raw, cleaned = lines[index]
        value = self._value_before_colon(cleaned)

        for difficulty in Difficulty:
            if difficulty.value.lower() == value.lower():
                return difficulty, index + 1

        allowed = ", ".join(d.value for d in Difficulty)
        raise ValueError(
            f"Línea 3 de cabecera inválida: difficulty {value!r} no reconocida "
            f"(valores permitidos: {allowed})"
        )

    def _read_meter(
        self,
        lines: list[tuple[str, str]],
        index: int,
    ) -> tuple[int, int]:
        raw, cleaned = lines[index]
        value = self._value_before_colon(cleaned)

        if not self.METER_PATTERN.match(value):
            raise ValueError(
                f"Línea 4 de cabecera inválida: meter debe ser un entero, "
                f"se obtuvo {value!r} en {raw!r}"
            )

        meter = int(value)

        if meter < 1:
            raise ValueError(
                f"Línea 4 de cabecera inválida: meter debe ser >= 1, "
                f"se obtuvo {meter}"
            )

        return meter, index + 1

    def _read_radar(
        self,
        lines: list[tuple[str, str]],
        index: int,
    ) -> tuple[str, int]:
        raw, cleaned = lines[index]

        if self.NOTE_ROW_PATTERN.match(cleaned.rstrip(",")):
            raise ValueError(
                "Línea 5 de cabecera inválida: se esperaba radar con valores "
                f"separados por coma, pero parece una fila de notas: {raw!r}"
            )

        value = self._value_before_colon(cleaned)

        if not self.RADAR_PATTERN.match(value):
            raise ValueError(
                "Línea 5 de cabecera inválida: radar mal formado "
                f"(se espera algo como '1.000,1.000,1.000,0.996,0.294'): {raw!r}"
            )

        return value, index + 1
