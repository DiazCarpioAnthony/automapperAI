from dataclasses import dataclass, field

from .bpm import BPM
from .chart import Chart


@dataclass
class Song:
    title: str
    subtitle: str
    artist: str

    music: str

    offset: float

    bpms: list[BPM] = field(default_factory=list)

    charts: list[Chart] = field(default_factory=list)