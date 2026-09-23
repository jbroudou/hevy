"""Domain helpers for grouping Hevy data."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

# Routines with a null folder_id live outside any folder in the Hevy app.
UNFILED_FOLDER_ID = None
UNFILED_TITLE = "(No folder)"


@dataclass
class Routine:
    """A single Hevy routine."""

    id: str
    title: str
    folder_id: int | None
    exercise_count: int
    updated_at: str | None
    created_at: str | None

    @classmethod
    def from_api(cls, data: dict[str, Any]) -> "Routine":
        return cls(
            id=data.get("id", ""),
            title=data.get("title") or "(untitled)",
            folder_id=data.get("folder_id"),
            exercise_count=len(data.get("exercises") or []),
            updated_at=data.get("updated_at"),
            created_at=data.get("created_at"),
        )


@dataclass
class Folder:
    """A routine folder, plus the routines it contains."""

    id: int | None
    title: str
    index: int
    routines: list[Routine] = field(default_factory=list)

    @classmethod
    def from_api(cls, data: dict[str, Any]) -> "Folder":
        return cls(
            id=data.get("id"),
            title=data.get("title") or "(untitled folder)",
            index=data.get("index", 0),
        )

    @classmethod
    def unfiled(cls) -> "Folder":
        """The pseudo-folder holding routines with no folder_id."""
        # Sorts last: real folder indexes start at 0.
        return cls(id=UNFILED_FOLDER_ID, title=UNFILED_TITLE, index=10**9)


def group_routines_by_folder(
    folders: list[dict[str, Any]],
    routines: list[dict[str, Any]],
) -> list[Folder]:
    """
    Group routines under their folders, ordered by the folder index used in
    the Hevy app. Folders with no routines are kept; routines whose folder is
    missing or null are collected under a trailing "(No folder)" entry.
    """
    grouped = {f["id"]: Folder.from_api(f) for f in folders}
    unfiled = Folder.unfiled()

    for raw in routines:
        routine = Routine.from_api(raw)
        folder = grouped.get(routine.folder_id, unfiled)
        folder.routines.append(routine)

    ordered = sorted(grouped.values(), key=lambda f: (f.index, f.title))
    if unfiled.routines:
        ordered.append(unfiled)

    for folder in ordered:
        folder.routines.sort(key=lambda r: r.title.lower())

    return ordered


@dataclass
class WorkoutSet:
    """One logged set. Which fields are populated depends on exercise type."""

    index: int
    type: str
    weight_kg: float | None
    reps: int | None
    distance_meters: float | None
    duration_seconds: int | None
    rpe: float | None

    @classmethod
    def from_api(cls, data: dict[str, Any]) -> "WorkoutSet":
        return cls(
            index=data.get("index", 0),
            type=data.get("type") or "normal",
            weight_kg=data.get("weight_kg"),
            reps=data.get("reps"),
            distance_meters=data.get("distance_meters"),
            duration_seconds=data.get("duration_seconds"),
            rpe=data.get("rpe"),
        )

    @property
    def volume_kg(self) -> float:
        """Weight x reps. Zero for sets that log distance or duration."""
        if self.weight_kg is None or self.reps is None:
            return 0.0
        return self.weight_kg * self.reps

    def describe(self) -> str:
        """Render the set the way it was logged, e.g. "5 kg x 20"."""
        parts: list[str] = []
        if self.weight_kg is not None:
            # Show a logged 0 kg rather than hiding it: on band work it means
            # the resistance was never recorded, which is worth seeing.
            parts.append(f"{format_number(self.weight_kg)} kg")
        if self.reps is not None:
            parts.append(f"x {self.reps}")
        if self.distance_meters is not None:
            parts.append(f"x {format_number(self.distance_meters)} m")
        if self.duration_seconds is not None:
            parts.append(f"x {format_duration(self.duration_seconds)}")
        if not parts:
            # A bodyweight set with no reps still happened; say so.
            return "logged"
        return " ".join(parts)


@dataclass
class WorkoutExercise:
    """One exercise within a logged workout."""

    index: int
    title: str
    notes: str
    template_id: str
    sets: list[WorkoutSet] = field(default_factory=list)

    @classmethod
    def from_api(cls, data: dict[str, Any]) -> "WorkoutExercise":
        return cls(
            index=data.get("index", 0),
            title=data.get("title") or "(untitled)",
            notes=data.get("notes") or "",
            template_id=data.get("exercise_template_id", ""),
            sets=[WorkoutSet.from_api(s) for s in data.get("sets") or []],
        )

    @property
    def volume_kg(self) -> float:
        return sum(s.volume_kg for s in self.sets)


@dataclass
class Workout:
    """A logged workout."""

    id: str
    title: str
    description: str
    routine_id: str | None
    start_time: str | None
    end_time: str | None
    exercises: list[WorkoutExercise] = field(default_factory=list)

    @classmethod
    def from_api(cls, data: dict[str, Any]) -> "Workout":
        return cls(
            id=data.get("id", ""),
            title=data.get("title") or "(untitled)",
            description=data.get("description") or "",
            routine_id=data.get("routine_id"),
            start_time=data.get("start_time"),
            end_time=data.get("end_time"),
            exercises=[
                WorkoutExercise.from_api(e) for e in data.get("exercises") or []
            ],
        )

    @property
    def started(self) -> datetime | None:
        """Start time in the local timezone."""
        return parse_time(self.start_time)

    @property
    def duration_seconds(self) -> int | None:
        """Elapsed wall-clock time, which includes rest and setup."""
        start, end = parse_time(self.start_time), parse_time(self.end_time)
        if start is None or end is None:
            return None
        return int((end - start).total_seconds())

    @property
    def total_sets(self) -> int:
        return sum(len(e.sets) for e in self.exercises)

    @property
    def total_reps(self) -> int:
        return sum(s.reps or 0 for e in self.exercises for s in e.sets)

    @property
    def total_volume_kg(self) -> float:
        return sum(e.volume_kg for e in self.exercises)


def parse_time(value: str | None) -> datetime | None:
    """Parse an API timestamp into local time, tolerating a trailing Z."""
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed.astimezone() if parsed.tzinfo else parsed


def format_number(value: float) -> str:
    """Drop the decimal point when a value is whole, e.g. 5.0 -> "5"."""
    return f"{value:g}"


def format_duration(seconds: int | None) -> str:
    """Render seconds as h:mm:ss, or m:ss under an hour."""
    if seconds is None:
        return "-"
    hours, rest = divmod(int(seconds), 3600)
    minutes, secs = divmod(rest, 60)
    if hours:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes}:{secs:02d}"
