from dataclasses import dataclass, field

from app.models.measure import Measure


@dataclass
class Chart:

    step_type: str = ""
    difficulty: str = ""
    level: int = 0

    measures: list[Measure] = field(default_factory=list)