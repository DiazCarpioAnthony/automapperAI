from dataclasses import dataclass, field

from app.models.metadata import Metadata
from app.models.timing import Timing
from app.models.chart import Chart


@dataclass
class Song:

    metadata: Metadata

    timing: Timing

    charts: list[Chart] = field(default_factory=list)