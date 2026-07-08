from dataclasses import dataclass, field


@dataclass
class Measure:
    rows: list[str] = field(default_factory=list)
