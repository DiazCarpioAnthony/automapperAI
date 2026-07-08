from enum import Enum


class Difficulty(Enum):

    BEGINNER = "Beginner"

    EASY = "Easy"

    MEDIUM = "Medium"

    HARD = "Hard"

    CHALLENGE = "Challenge"

    EDIT = "Edit"


class Lane(Enum):
    """Carriles de dance-single (4) y dance-double (8)."""

    LEFT = 0
    DOWN = 1
    UP = 2
    RIGHT = 3
    LEFT_P2 = 4
    DOWN_P2 = 5
    UP_P2 = 6
    RIGHT_P2 = 7


class NoteType(Enum):
    """Tipos de nota según el carácter del .sm."""

    TAP = "1"
    HOLD_START = "2"
    HOLD_END = "3"
    ROLL_START = "4"
    MINE = "M"
    LIFT = "L"
    FAKE = "F"
    KEYSOUND = "K"
    # R aparece en NOTE_ROW_PATTERN de charts legacy; lo tratamos como tipo propio
    R = "R"