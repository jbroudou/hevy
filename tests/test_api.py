"""Tests for the Hevy API client."""

import httpx
import pytest

from hevy.api import HevyAPIError, HevyClient


def make_client(handler) -> HevyClient:
    client = HevyClient(api_key="test-key", base_url="https://example.test")
    client._client = httpx.Client(
        base_url="https://example.test",
        headers={"api-key": "test-key"},
        transport=httpx.MockTransport(handler),
    )
    return client


def test_paginate_walks_every_page_and_caps_page_size():
    seen_params = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen_params.append(dict(request.url.params))
        page = int(request.url.params["page"])
        return httpx.Response(
            200, json={"page": page, "page_count": 3, "routines": [{"id": page}]}
        )

    with make_client(handler) as client:
        items = list(client.paginate("/v1/routines", "routines", page_size=100))

    assert [i["id"] for i in items] == [1, 2, 3]
    assert all(p["pageSize"] == "10" for p in seen_params)


def test_paginate_stops_on_an_empty_page():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"page_count": 99, "routines": []})

    with make_client(handler) as client:
        assert list(client.paginate("/v1/routines", "routines")) == []


def test_api_error_surfaces_status_and_message():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(401, json={"error": "Invalid api-key"})

    with make_client(handler) as client, pytest.raises(HevyAPIError) as excinfo:
        client.get("/v1/routines")

    assert excinfo.value.status_code == 401
    assert "Invalid api-key" in excinfo.value.message


def test_api_key_is_sent_as_a_header():
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers["api-key"] == "test-key"
        return httpx.Response(200, json={"page_count": 1, "routine_folders": []})

    with make_client(handler) as client:
        assert client.list_routine_folders() == []


def test_unwrap_routine_handles_both_response_shapes():
    from hevy.api import unwrap_routine

    # GET /v1/routines/{id} nests a single object.
    assert unwrap_routine({"routine": {"id": "a"}})["id"] == "a"
    # POST /v1/routines nests a one-item list.
    assert unwrap_routine({"routine": [{"id": "b"}]})["id"] == "b"
    assert unwrap_routine({"routine": []}) == {}


def test_post_tolerates_an_empty_body():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(201, content=b"")

    with make_client(handler) as client:
        assert client.post("/v1/exercise_templates", {"exercise": {}}) == {}


def test_update_routine_puts_to_the_routine_path():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["method"] = request.method
        seen["path"] = request.url.path
        return httpx.Response(200, json={"routine": [{"id": "r1", "title": "T"}]})

    with make_client(handler) as client:
        response = client.update_routine("r1", {"title": "T", "exercises": []})

    assert seen == {"method": "PUT", "path": "/v1/routines/r1"}
    assert response["routine"][0]["id"] == "r1"


def test_request_retries_on_429_then_succeeds(monkeypatch):
    monkeypatch.setattr("hevy.api.time.sleep", lambda _: None)
    calls = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        if calls["n"] < 3:
            return httpx.Response(429, headers={"Retry-After": "0"})
        return httpx.Response(200, json={"routine": [{"id": "ok"}]})

    with make_client(handler) as client:
        assert client.post("/v1/routines", {"routine": {}})["routine"][0]["id"] == "ok"
    assert calls["n"] == 3


def test_request_gives_up_after_max_retries(monkeypatch):
    monkeypatch.setattr("hevy.api.time.sleep", lambda _: None)

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(429, headers={"Retry-After": "0"})

    with make_client(handler) as client, pytest.raises(HevyAPIError) as excinfo:
        client.post("/v1/routines", {"routine": {}})
    assert excinfo.value.status_code == 429
