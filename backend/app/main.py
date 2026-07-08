from app.config import SAMPLE_DIR
from app.parser.note_parser import NoteParser
from app.parser.sm_parser import SMParser

song_path = SAMPLE_DIR / "Black or White Mondaiji" / "Black or White.sm"

parser = SMParser()
song = parser.parse(song_path)

print("=== Song ===")
print(f"Title:  {song.metadata.title}")
print(f"Artist: {song.metadata.artist}")
print(f"BPMs:   {song.timing.bpms}")
print()

print(f"Charts: {len(song.charts)}")
print()

for index, chart in enumerate(song.charts, start=1):
    total_rows = sum(len(measure.rows) for measure in chart.measures)

    print(f"Chart {index}:")
    print(f"  step_type:   {chart.step_type}")
    print(f"  difficulty:  {chart.difficulty}")
    print(f"  meter:       {chart.meter}")
    print(f"  measures:    {len(chart.measures)}")
    print(f"  total rows:  {total_rows}")
    print()

# Commit 4: NoteParser todavía no está en el pipeline.
# Se prueba aquí sobre filas reales del primer chart.
note_parser = NoteParser()
sample_rows = [
    row
    for measure in song.charts[0].measures
    for row in measure.rows
    if row != "0000"
][:8]

print("=== NoteParser (commit 4) ===")
for row in sample_rows:
    notes = note_parser.parse(row)
    rendered = ", ".join(
        f"{note.lane.name}:{note.type.name}" for note in notes
    ) or "(vacío)"
    print(f"  {row}  ->  [{rendered}]")
