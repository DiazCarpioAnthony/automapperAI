from dataclasses import dataclass, field

from app.core.enums import Difficulty
from app.models.measure import Measure


@dataclass
class Chart:

    step_type: str = ""

    description: str = ""

    difficulty: Difficulty | None = None

    meter: int = 0

    radar: str = ""

    measures: list[Measure] = field(default_factory=list)