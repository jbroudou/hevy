"""Tests for routine/folder grouping."""

from hevy.models import UNFILED_TITLE, group_routines_by_folder

FOLDERS = [
    {"id": 2, "index": 1, "title": "Heatrick"},
    {"id": 1, "index": 0, "title": "Quick Gym"},
    {"id": 3, "index": 2, "title": "Empty"},
]

ROUTINES = [
    {"id": "r1", "title": "Push", "folder_id": 1, "exercises": [{}, {}]},
    {"id": "r2", "title": "abs", "folder_id": 1, "exercises": []},
    {"id": "r3", "title": "Power A", "folder_id": 2, "exercises": [{}]},
    {"id": "r4", "title": "Scratch", "folder_id": None, "exercises": [{}]},
]


def test_folders_are_ordered_by_index_with_unfiled_last():
    grouped = group_routines_by_folder(FOLDERS, ROUTINES)
    assert [f.title for f in grouped] == [
        "Quick Gym",
        "Heatrick",
        "Empty",
        UNFILED_TITLE,
    ]


def test_routines_land_in_their_folder():
    grouped = {f.title: f for f in group_routines_by_folder(FOLDERS, ROUTINES)}
    assert [r.id for r in grouped["Quick Gym"].routines] == [
        "r2",
        "r1",
    ]  # case-insensitive sort
    assert grouped["Empty"].routines == []
    assert [r.id for r in grouped[UNFILED_TITLE].routines] == ["r4"]


def test_exercise_count_and_unknown_folder_falls_back_to_unfiled():
    orphan = [
        {"id": "r9", "title": "Ghost", "folder_id": 999, "exercises": [{}, {}, {}]}
    ]
    grouped = group_routines_by_folder(FOLDERS, orphan)
    unfiled = grouped[-1]
    assert unfiled.title == UNFILED_TITLE
    assert unfiled.routines[0].exercise_count == 3


def test_unfiled_folder_is_omitted_when_everything_is_filed():
    filed = [r for r in ROUTINES if r["folder_id"] == 1]
    grouped = group_routines_by_folder(FOLDERS, filed)
    assert all(f.title != UNFILED_TITLE for f in grouped)
