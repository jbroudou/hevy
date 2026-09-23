"""Thin client for the Hevy public API (https://api.hevyapp.com/docs/)."""

import contextlib
import itertools
import time
from collections.abc import Iterator
from typing import Any

import httpx

from .config import Config, config
from .logger import logger


class HevyAPIError(RuntimeError):
    """Raised when the Hevy API returns an error response."""

    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(f"Hevy API error {status_code}: {message}")


def unwrap_workout(payload: dict[str, Any]) -> dict[str, Any]:
    """
    Pull the workout object out of a response.

    GET /v1/workouts/{id} returns the workout unwrapped, but the write
    endpoints nest it under "workout" the way routines do.
    """
    workout = payload.get("workout", payload)
    if isinstance(workout, list):
        return workout[0] if workout else {}
    return workout


def unwrap_routine(payload: dict[str, Any]) -> dict[str, Any]:
    """
    Pull the routine object out of a response.

    The API is inconsistent here: GET /v1/routines/{id} nests a single object
    under "routine", while POST /v1/routines nests a one-item list.
    """
    routine = payload.get("routine", payload)
    if isinstance(routine, list):
        return routine[0] if routine else {}
    return routine


class HevyClient:
    """
    Client for the Hevy public API.

    Authentication is a single `api-key` header. Every paginated endpoint
    accepts `page` (1-based) and `pageSize` (max 10) and returns a
    `page_count` field alongside the payload.
    """

    #: Attempts and base backoff used when the API answers 429.
    MAX_RETRIES = 5
    RETRY_BACKOFF_SECONDS = 3.0

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        timeout: float = 30.0,
    ):
        self.api_key = api_key or config.HEVY_API_KEY
        self.base_url = (base_url or config.HEVY_API_BASE_URL).rstrip("/")
        self._client = httpx.Client(
            base_url=self.base_url,
            headers={"api-key": self.api_key, "Accept": "application/json"},
            timeout=timeout,
        )

    def __enter__(self) -> "HevyClient":
        return self

    def __exit__(self, *exc_info) -> None:
        self.close()

    def close(self) -> None:
        self._client.close()

    # -- low level ---------------------------------------------------------

    def _request(self, method: str, path: str, **kwargs: Any) -> httpx.Response:
        """Issue a request, retrying with backoff while the API answers 429."""
        for attempt in range(self.MAX_RETRIES):
            response = self._client.request(method, path, **kwargs)
            if response.status_code != 429:
                return response

            # Honour Retry-After when present, else back off linearly.
            retry_after = response.headers.get("Retry-After")
            try:
                delay = float(retry_after) if retry_after else 0.0
            except ValueError:
                delay = 0.0
            delay = delay or self.RETRY_BACKOFF_SECONDS * (attempt + 1)

            logger.warning(
                "%s %s rate limited (attempt %d/%d), retrying in %.0fs",
                method,
                path,
                attempt + 1,
                self.MAX_RETRIES,
                delay,
            )
            time.sleep(delay)

        return response

    def get(self, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        """GET a path and return the decoded JSON body."""
        logger.debug("GET %s params=%s", path, params)
        response = self._request("GET", path, params=params)

        if response.status_code >= 400:
            message = response.text
            with contextlib.suppress(ValueError):
                message = response.json().get("error", message)
            logger.error("GET %s -> %s: %s", path, response.status_code, message)
            raise HevyAPIError(response.status_code, message)

        return response.json()

    def paginate(
        self,
        path: str,
        key: str,
        page_size: int = Config.HEVY_MAX_PAGE_SIZE,
        params: dict[str, Any] | None = None,
    ) -> Iterator[dict[str, Any]]:
        """
        Yield every item from a paginated endpoint.

        Args:
            path: Endpoint path, e.g. "/v1/routines".
            key: Name of the list field in the response, e.g. "routines".
            page_size: Items per request (the API caps this at 10).
            params: Extra query parameters.
        """
        page_size = min(page_size, Config.HEVY_MAX_PAGE_SIZE)
        page = 1

        while True:
            query = dict(params or {})
            query.update({"page": page, "pageSize": page_size})
            payload = self.get(path, params=query)

            items = payload.get(key) or []
            yield from items

            page_count = payload.get("page_count") or 1
            if page >= page_count or not items:
                break
            page += 1

    # -- endpoints ---------------------------------------------------------

    def list_routine_folders(self) -> list:
        """Return every routine folder on the account."""
        return list(self.paginate("/v1/routine_folders", "routine_folders"))

    def list_routines(self) -> list:
        """Return every routine on the account."""
        return list(self.paginate("/v1/routines", "routines"))

    def get_routine(self, routine_id: str) -> dict[str, Any]:
        """Return a single routine by id."""
        payload = self.get(f"/v1/routines/{routine_id}")
        return unwrap_routine(payload)

    def list_workouts(self, limit: int | None = None) -> list:
        """
        Return logged workouts, newest first.

        The API returns them in reverse chronological order, so `limit` reads
        only as many pages as it needs rather than walking the whole history.
        """
        pages = self.paginate("/v1/workouts", "workouts")
        if limit is not None:
            return list(itertools.islice(pages, limit))
        return list(pages)

    def get_workout(self, workout_id: str) -> dict[str, Any]:
        """Return a single logged workout by id."""
        return unwrap_workout(self.get(f"/v1/workouts/{workout_id}"))

    def count_workouts(self) -> int:
        """Return the total number of logged workouts."""
        return self.get("/v1/workouts/count").get("workout_count", 0)

    def get_user_info(self) -> dict[str, Any]:
        """Return the authenticated user's info."""
        return self.get("/v1/user/info")

    # -- writes ------------------------------------------------------------

    def post(self, path: str, payload: dict[str, Any]) -> dict[str, Any]:
        """POST a JSON body and return the decoded JSON response."""
        return self._write("POST", path, payload)

    def put(self, path: str, payload: dict[str, Any]) -> dict[str, Any]:
        """PUT a JSON body and return the decoded JSON response."""
        return self._write("PUT", path, payload)

    def _write(self, method: str, path: str, payload: dict[str, Any]) -> dict[str, Any]:
        logger.debug("%s %s payload=%s", method, path, payload)
        response = self._request(method, path, json=payload)

        if response.status_code >= 400:
            message = response.text
            with contextlib.suppress(ValueError):
                message = response.json().get("error", message)
            logger.error("%s %s -> %s: %s", method, path, response.status_code, message)
            raise HevyAPIError(response.status_code, message)

        # Some write endpoints answer 2xx with an empty or non-JSON body.
        if not response.content:
            return {}
        try:
            return response.json()
        except ValueError:
            logger.warning("%s %s returned a non-JSON body", method, path)
            return {}

    def list_exercise_templates(self) -> list:
        """Return every exercise template available on the account."""
        return list(self.paginate("/v1/exercise_templates", "exercise_templates"))

    def create_exercise_template(
        self,
        title: str,
        exercise_type: str,
        equipment_category: str,
        muscle_group: str,
        other_muscles: list[str] | None = None,
    ) -> dict[str, Any]:
        """Create a custom exercise template and return it."""
        return self.post(
            "/v1/exercise_templates",
            {
                "exercise": {
                    "title": title,
                    "exercise_type": exercise_type,
                    "equipment_category": equipment_category,
                    "muscle_group": muscle_group,
                    "other_muscles": other_muscles or [],
                }
            },
        )

    def create_routine_folder(self, title: str) -> dict[str, Any]:
        """Create a routine folder. Hevy inserts it at index 0."""
        return self.post("/v1/routine_folders", {"routine_folder": {"title": title}})

    def create_routine(self, routine: dict[str, Any]) -> dict[str, Any]:
        """Create a routine from a fully-formed routine payload."""
        return self.post("/v1/routines", {"routine": routine})

    def update_routine(
        self, routine_id: str, routine: dict[str, Any]
    ) -> dict[str, Any]:
        """Replace a routine in place. Every exercise and set is overwritten."""
        return self.put(f"/v1/routines/{routine_id}", {"routine": routine})
