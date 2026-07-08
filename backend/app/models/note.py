from dataclasses import dataclass

from app.core.enums import Lane, NoteType


@dataclass
class Note:

    lane: Lane

    type: NoteType
