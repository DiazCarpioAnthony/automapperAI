from app.config import SAMPLE_DIR
from app.parser.sm_parser import SMParser

song = SAMPLE_DIR / "Black or White Mondaiji" / "Black or White.sm"

parser = SMParser()

parser.parse(song)