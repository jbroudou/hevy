"""Build Hevy routine payloads from a JSON spec file."""

import json
from pathlib import Path
from typing import Any

from .api import HevyClient
from .logger import logger


class SpecError(RuntimeError):
    """Raised when a routine spec is invalid or cannot be resolved."""


def load_spec(path: Path) -> dict[str, Any]:
    """Load and minimally validate a routine spec file."""
    try:
        spec = json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        raise SpecError(f"{path} is not valid JSON: {exc}") from exc

    if not spec.get("title"):
        raise SpecError(f"{path} is missing a 'title'.")
    if not spec.get("exercises"):
        raise SpecError(f"{path} has no 'exercises'.")
    return spec


def resolve_folder_id(client: HevyClient, name: str | None) -> int | None:
    """Look up a folder id by title. Returns None for the default folder."""
    if not name:
        return None
    folders = client.list_routine_folders()
    for folder in folders:
        if folder["title"].strip().lower() == name.strip().lower():
            return folder["id"]
    known = ", ".join(sorted(f["title"] for f in folders))
    raise SpecError(f"No folder titled {name!r}. Existing folders: {known}.")


def _refetch_template(client: HevyClient, title: str) -> dict[str, Any]:
    """Read a just-created template back by title to recover its id."""
    wanted = title.strip().lower()
    for template in client.list_exercise_templates():
        if template["title"].strip().lower() == wanted:
            return template
    raise SpecError(f"Created template {title!r} but could not read it back.")


def resolve_exercises(
    client: HevyClient,
    spec: dict[str, Any],
    create_missing: bool = True,
) -> tuple[list[dict[str, Any]], list[str]]:
    """
    Turn spec exercises into API payload exercises.

    Each spec exercise is matched to a template by explicit ``template_id``, or
    by exact title against the account's templates. An entry carrying a
    ``create`` block is created as a custom template when no title matches.

    Returns the payload exercises and a list of titles that were created.
    """
    templates = client.list_exercise_templates()
    by_title = {t["title"].strip().lower(): t for t in templates}
    by_id = {t["id"]: t for t in templates}

    payload_exercises: list[dict[str, Any]] = []
    created: list[str] = []

    for entry in spec["exercises"]:
        name = entry.get("name", "")
        template_id = entry.get("template_id")

        if template_id:
            if template_id not in by_id:
                raise SpecError(f"Unknown template_id {template_id!r} for {name!r}.")
            resolved = by_id[template_id]
        elif name.strip().lower() in by_title:
            resolved = by_title[name.strip().lower()]
            logger.info("Reusing existing template %r (%s)", name, resolved["id"])
        elif entry.get("create"):
            if not create_missing:
                # Dry runs must not write, so stand in a placeholder. Reaching
                # here means no existing template matched, so this title really
                # would be created -- report it as such.
                resolved = {"id": "<to be created>", "title": name}
                created.append(name)
            else:
                response = client.create_exercise_template(
                    title=name, **entry["create"]
                )
                resolved = response.get("exercise_template", response)
                if not resolved.get("id"):
                    # This endpoint can answer with an empty body, so read the
                    # new template back by title to recover its id.
                    resolved = _refetch_template(client, name)
                by_title[name.strip().lower()] = resolved
                created.append(name)
                logger.info("Created custom template %r (%s)", name, resolved["id"])
        else:
            raise SpecError(
                f"No template matches {name!r} and the spec gives no 'create' block."
            )

        sets = [
            {
                "type": "normal",
                "weight_kg": entry.get("weight_kg"),
                "reps": entry.get("reps"),
                "distance_meters": entry.get("distance_meters"),
                "duration_seconds": entry.get("duration_seconds"),
                "custom_metric": None,
            }
            for _ in range(entry.get("sets", 1))
        ]

        payload_exercises.append(
            {
                "exercise_template_id": resolved["id"],
                "superset_id": entry.get("superset_id"),
                "rest_seconds": entry.get("rest_seconds"),
                "notes": entry.get("notes"),
                "sets": sets,
            }
        )

    return payload_exercises, created


def build_routine_payload(
    client: HevyClient,
    spec: dict[str, Any],
    create_missing: bool = True,
) -> tuple[dict[str, Any], list[str]]:
    """Build the full POST /v1/routines payload from a spec."""
    folder_id = resolve_folder_id(client, spec.get("folder"))
    exercises, created = resolve_exercises(client, spec, create_missing=create_missing)
    payload = {
        "title": spec["title"],
        "folder_id": folder_id,
        "notes": spec.get("notes", ""),
        "exercises": exercises,
    }
    return payload, created
