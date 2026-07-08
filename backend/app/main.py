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
    first_measure = chart.measures[0]
    last_measure = chart.measures[-1]

    print(f"Chart {index}:")
    print(f"  step_type:   {chart.step_type}")
    print(f"  difficulty:  {chart.difficulty}")
    print(f"  meter:       {chart.meter}")
    print(f"  measures:    {len(chart.measures)}")
    print(f"  total rows:  {total_rows}")
    print(f"  measure 1:   {len(first_measure.rows)} rows -> {first_measure.rows[:4]} ...")
    print(f"  measure {len(chart.measures)}: {len(last_measure.rows)} rows -> {last_measure.rows[:4]} ...")
    print()
