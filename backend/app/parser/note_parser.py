from app.core.enums import Lane, NoteType
from app.models.note import Note
from app.parser.chart_header_parser import ChartHeaderParser


class NoteParser:
    """
    Convierte una fila cruda del .sm en notas.

    Ejemplo:
        "0230" → [
            Note(lane=DOWN, type=HOLD_START),
            Note(lane=UP,   type=HOLD_END),
        ]
    """

    NOTE_ROW_PATTERN = ChartHeaderParser.NOTE_ROW_PATTERN

    # Índice de columna → Lane (dance-single / dance-double)
    LANES = (
        Lane.LEFT,
        Lane.DOWN,
        Lane.UP,
        Lane.RIGHT,
        Lane.LEFT_P2,
        Lane.DOWN_P2,
        Lane.UP_P2,
        Lane.RIGHT_P2,
    )

    CHAR_TO_NOTE_TYPE = {note_type.value: note_type for note_type in NoteType}

    def parse(self, row: str) -> list[Note]:
        cleaned = row.strip()

        if not self.NOTE_ROW_PATTERN.match(cleaned):
            raise ValueError(f"Fila de notas inválida: {row!r}")

        notes: list[Note] = []

        for index, char in enumerate(cleaned):
            if char == "0":
                continue

            note_type = self.CHAR_TO_NOTE_TYPE.get(char)

            if note_type is None:
                raise ValueError(
                    f"Carácter de nota no reconocido {char!r} "
                    f"en fila {row!r} (columna {index})"
                )

            notes.append(
                Note(
                    lane=self.LANES[index],
                    type=note_type,
                )
            )

        return notes
