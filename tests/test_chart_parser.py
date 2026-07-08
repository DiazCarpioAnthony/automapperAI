import pytest

from app.config import SAMPLE_DIR
from app.core.enums import Difficulty, Lane, NoteType
from app.parser.chart_header_parser import ChartHeaderParser
from app.parser.chart_parser import ChartParser
from app.parser.measure_parser import MeasureParser
from app.parser.note_parser import NoteParser
from app.parser.sm_parser import SMParser


SAMPLE_SM = SAMPLE_DIR / "Black or White Mondaiji" / "Black or White.sm"

MINI_BLOCK = """\
dance-single:
:
Hard:
7:
1.000,1.000,1.000,0.996,0.294:
0020
0230
,
0000
1101
,
"""


def count_rows(charts) -> list[int]:
    return [
        sum(len(measure.rows) for measure in chart.measures)
        for chart in charts
    ]


def count_notes(charts) -> list[int]:
    return [
        sum(
            len(notes)
            for measure in chart.measures
            for notes in measure.notes_by_row
        )
        for chart in charts
    ]


def test_sm_parser_parses_sample_song():
    song = SMParser().parse(SAMPLE_SM)

    assert song.metadata.title == "Black or White"
    assert song.metadata.artist == "Nomizu Iori"
    assert len(song.charts) == 2


def test_chart_parser_sample_counts():
    text = SAMPLE_SM.read_text(encoding="utf-8")
    charts = ChartParser().parse(text)

    assert len(charts) == 2
    assert all(chart.step_type == "dance-single" for chart in charts)
    assert charts[0].difficulty == Difficulty.HARD
    assert charts[1].difficulty == Difficulty.CHALLENGE
    assert [chart.meter for chart in charts] == [7, 8]
    assert [len(chart.measures) for chart in charts] == [65, 65]
    assert count_rows(charts) == [736, 848]
    assert count_notes(charts) == [898, 1092]


def test_chart_header_parser_splits_header_and_body():
    parser = ChartHeaderParser()
    chart, body = parser.split(MINI_BLOCK)

    assert chart.step_type == "dance-single"
    assert chart.description == ""
    assert chart.difficulty == Difficulty.HARD
    assert chart.meter == 7
    assert "0020" in body
    assert "1101" in body


def test_measure_parser_builds_measures_and_notes():
    _chart, body = ChartHeaderParser().split(MINI_BLOCK)
    measures = MeasureParser().parse(body)

    assert len(measures) == 2
    assert measures[0].rows == ["0020", "0230"]
    assert measures[1].rows == ["0000", "1101"]
    assert len(measures[0].notes_by_row) == 2
    assert len(measures[0].notes_by_row[0]) == 1
    assert len(measures[0].notes_by_row[1]) == 2
    assert len(measures[1].notes_by_row[1]) == 3


def test_note_parser_maps_row_to_lane_and_type():
    notes = NoteParser().parse("0230")

    assert len(notes) == 2
    assert notes[0].lane == Lane.DOWN
    assert notes[0].type == NoteType.HOLD_START
    assert notes[1].lane == Lane.UP
    assert notes[1].type == NoteType.HOLD_END


def test_note_parser_rejects_invalid_row():
    with pytest.raises(ValueError, match="Fila de notas inválida"):
        NoteParser().parse("abcd")


def test_chart_header_parser_rejects_incomplete_header():
    with pytest.raises(ValueError, match="Cabecera #NOTES: incompleta"):
        ChartHeaderParser().split("dance-single:\n:\nHard:\n")


def test_measure_parser_rejects_invalid_body_line():
    with pytest.raises(ValueError, match="Línea de notas inválida"):
        MeasureParser().parse("0020\nbad-row\n,")
