from app.config import SAMPLE_DIR
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
    total_notes = sum(
        len(notes)
        for measure in chart.measures
        for notes in measure.notes_by_row
    )

    print(f"Chart {index}:")
    print(f"  step_type:   {chart.step_type}")
    print(f"  difficulty:  {chart.difficulty}")
    print(f"  meter:       {chart.meter}")
    print(f"  measures:    {len(chart.measures)}")
    print(f"  total rows:  {total_rows}")
    print(f"  total notes: {total_notes}")
    print()

# Commit 5: notes_by_row ya viene desde el pipeline.
sample = [
    (row, notes)
    for measure in song.charts[0].measures
    for row, notes in zip(measure.rows, measure.notes_by_row)
    if row != "0000"
][:8]

print("=== NotesByRow (commit 5) ===")
for row, notes in sample:
    rendered = ", ".join(
        f"{note.lane.name}:{note.type.name}" for note in notes
    ) or "(vacío)"
    print(f"  {row}  ->  [{rendered}]")
