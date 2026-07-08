from dataclasses import dataclass, field

from app.models.note import Note


@dataclass
class Measure:
    notes: list[Note] = field(default_factory=list)