import re


class ChartParser:

    def parse(self, text: str) -> list[str]:
        """
        Extrae cada bloque #NOTES: completo del archivo .sm.
        Por ahora devuelve una lista de strings.
        """

        pattern = r"#NOTES:(.*?);"

        matches = re.findall(
            pattern,
            text,
            re.DOTALL
        )

        charts = []

        for match in matches:
            charts.append(match.strip())

        return charts