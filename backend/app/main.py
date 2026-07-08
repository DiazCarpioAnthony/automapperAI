from app.config import SAMPLE_DIR
from app.parser.chart_parser import ChartParser
from app.parser.chart_header_parser import ChartHeaderParser
from app.parser.sm_parser import SMParser

song_path = SAMPLE_DIR / "Black or White Mondaiji" / "Black or White.sm"
text = song_path.read_text(encoding="utf-8", errors="replace")

sm_parser = SMParser()
chart_parser = ChartParser()
header_parser = ChartHeaderParser()

song = sm_parser.parse(song_path)
blocks = chart_parser.parse(text)
parsed_charts = [header_parser.split(block) for block in blocks]

print("=== Song (metadata + timing) ===")
print(f"Title:  {song.metadata.title}")
print(f"Artist: {song.metadata.artist}")
print(f"BPMs:   {song.timing.bpms}")
print()

print("=== Chart headers (commit 2) ===")
print(f"Bloques #NOTES: encontrados: {len(blocks)}")
print()

for index, (chart, body) in enumerate(parsed_charts, start=1):
    body_lines = [line for line in body.splitlines() if line.strip()]

    print(f"Chart {index}:")
    print(f"  step_type:   {chart.step_type}")
    print(f"  description: {chart.description!r}")
    print(f"  difficulty:  {chart.difficulty}")
    print(f"  meter:       {chart.meter}")
    print(f"  radar:       {chart.radar}")
    print(f"  body lines:  {len(body_lines)} (listo para commit 3)")
    print(f"  measures:    {len(chart.measures)}")
    print()
