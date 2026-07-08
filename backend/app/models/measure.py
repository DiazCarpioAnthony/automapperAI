from dataclasses import dataclass, field
from .row import Row


@dataclass
class Measure:
    index: int
    rows: list[Row] = field(default_factory=list)

    @property
    def subdivisions(self) -> int:
        return len(self.rows)