from dataclasses import dataclass, field

from .measure import Measure


@dataclass
class Chart:
    style: str
    difficulty: str
    level: int
    radar_values: list[float]

    measures: list[Measure] = field(default_factory=list)