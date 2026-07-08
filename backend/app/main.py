from app.config import SAMPLE_DIR
from app.parser.sm_parser import SMParser

song_path = SAMPLE_DIR / "Black or White Mondaiji" / "Black or White.sm"

parser = SMParser()

song = parser.parse(song_path)

print(song)
print()
print(f"Charts encontrados: {len(song.charts)}")