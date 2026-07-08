from dataclasses import dataclass


@dataclass
class Metadata:
    title: str = ""
    subtitle: str = ""

    artist: str = ""

    title_translit: str = ""
    subtitle_translit: str = ""
    artist_translit: str = ""

    credit: str = ""

    banner: str = ""
    background: str = ""
    cd_title: str = ""
    lyrics_path: str = ""

    music: str = ""

    offset: float = 0.0

    sample_start: float = 0.0
    sample_length: float = 0.0

    selectable: bool = True