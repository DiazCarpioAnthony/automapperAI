from dataclasses import dataclass, field

from app.models.note import Note


@dataclass
class Measure:
    rows: list[str] = field(default_factory=list)

    notes_by_row: list[list[Note]] = field(default_factory=list)
