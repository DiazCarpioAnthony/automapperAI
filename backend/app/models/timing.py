from dataclasses import dataclass, field


@dataclass
class BPMChange:
    beat: float
    bpm: float


@dataclass
class Stop:
    beat: float
    duration: float


@dataclass
class Timing:
    bpms: list[BPMChange] = field(default_factory=list)
    stops: list[Stop] = field(default_factory=list)