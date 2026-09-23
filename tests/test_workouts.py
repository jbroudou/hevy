"""Tests for workout parsing and the workout endpoints."""

import httpx
import pytest

from hevy.api import HevyClient, unwrap_workout
from hevy.models import Workout, WorkoutSet, format_duration, format_number


def make_client(handler) -> HevyClient:
    client = HevyClient(api_key="test-key", base_url="https://example.test")
    client._client = httpx.Client(
        transport=httpx.MockTransport(handler),
        base_url="https://example.test",
        headers={"api-key": "test-key"},
    )
    return client


WORKOUT = {
    "id": "w1",
    "title": "Shoulder Rehab",
    "description": "",
    "routine_id": "r1",
    "start_time": "2026-08-25T22:51:12+00:00",
    "end_time": "2026-08-25T23:40:09+00:00",
    "exercises": [
        {
            "index": 0,
            "title": "Cable External Rotation (Elbow at Side)",
            "notes": "",
            "exercise_template_id": "t1",
            "sets": [
                {"index": 0, "type": "normal", "weight_kg": 5, "reps": 20},
                {"index": 1, "type": "normal", "weight_kg": 5, "reps": 14},
            ],
        },
        {
            "index": 1,
            "title": "Upside Down Kettlebell Carry",
            "notes": "",
            "exercise_template_id": "t2",
            "sets": [
                {
                    "index": 0,
                    "type": "normal",
                    "weight_kg": 5,
                    "reps": None,
                    "distance_meters": 20,
                }
            ],
        },
    ],
}


def test_unwrap_workout_handles_both_shapes():
    assert unwrap_workout({"id": "w1"})["id"] == "w1"
    assert unwrap_workout({"workout": {"id": "w2"}})["id"] == "w2"
    assert unwrap_workout({"workout": [{"id": "w3"}]})["id"] == "w3"
    assert unwrap_workout({"workout": []}) == {}


def test_workout_totals_ignore_distance_sets():
    workout = Workout.from_api(WORKOUT)
    assert workout.total_sets == 3
    # The carry logs distance, not reps, so it adds nothing to reps or volume.
    assert workout.total_reps == 34
    assert workout.total_volume_kg == 5 * 20 + 5 * 14
    assert workout.duration_seconds == 2937


def test_set_describe_covers_each_logged_shape():
    weight = WorkoutSet.from_api({"weight_kg": 5, "reps": 20})
    assert weight.describe() == "5 kg x 20"

    # A zero weight is shown rather than hidden: on band work it means the
    # resistance was never recorded.
    zero = WorkoutSet.from_api({"weight_kg": 0, "reps": 15})
    assert zero.describe() == "0 kg x 15"

    carry = WorkoutSet.from_api({"weight_kg": 5, "distance_meters": 20})
    assert carry.describe() == "5 kg x 20 m"

    plank = WorkoutSet.from_api({"duration_seconds": 90})
    assert plank.describe() == "x 1:30"

    assert WorkoutSet.from_api({}).describe() == "logged"


def test_list_workouts_stops_at_the_limit():
    pages = []

    def handler(request: httpx.Request) -> httpx.Response:
        pages.append(request.url.params["page"])
        return httpx.Response(
            200, json={"page": 1, "page_count": 28, "workouts": [WORKOUT] * 10}
        )

    client = make_client(handler)
    workouts = client.list_workouts(limit=12)

    assert len(workouts) == 12
    # Twelve items need two pages of ten, not all twenty-eight.
    assert pages == ["1", "2"]


def test_get_workout_unwraps_the_bare_object():
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/v1/workouts/w1"
        return httpx.Response(200, json=WORKOUT)

    assert make_client(handler).get_workout("w1")["title"] == "Shoulder Rehab"


def test_count_workouts():
    client = make_client(lambda r: httpx.Response(200, json={"workout_count": 42}))
    assert client.count_workouts() == 42


@pytest.mark.parametrize(
    ("seconds", "expected"),
    [(None, "-"), (59, "0:59"), (90, "1:30"), (2937, "48:57"), (3661, "1:01:01")],
)
def test_format_duration(seconds, expected):
    assert format_duration(seconds) == expected


def test_format_number_drops_trailing_zeros():
    assert format_number(5.0) == "5"
    assert format_number(2.5) == "2.5"
