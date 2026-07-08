from app.config import SAMPLE_DIR
from app.parser.sm_parser import SMParser

sm_path = SAMPLE_DIR / "Black or White Mondaiji" / "Black or White.sm"

parser = SMParser()

song = parser.parse(sm_path)