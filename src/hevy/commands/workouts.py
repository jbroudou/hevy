"""`hevy workouts` commands."""

import json

import typer
from rich.console import Console
from rich.table import Table

from ..api import HevyClient
from ..logger import logger
from ..models import Workout, format_duration, format_number

app = typer.Typer(help="Inspect your logged Hevy workouts.")
console = Console()

#: How many recent workouts --routine scans before giving up. The API pages ten
#: at a time, so this is a deliberate ceiling on how much history we fetch.
DEFAULT_SEARCH_LIMIT = 50


def _matches_routine(workout: Workout, needle: str) -> bool:
    """Match a workout to a routine by title, case-insensitively."""
    return needle.strip().lower() in workout.title.strip().lower()


def _find_workout(
    client: HevyClient, routine: str | None, search_limit: int
) -> Workout:
    """Return the most recent workout, optionally filtered by routine title."""
    recent = [Workout.from_api(w) for w in client.list_workouts(limit=search_limit)]
    if not recent:
        raise typer.BadParameter("No workouts have been logged on this account.")

    if routine is None:
        return recent[0]

    for workout in recent:
        if _matches_routine(workout, routine):
            return workout

    raise typer.BadParameter(
        f"No workout titled like {routine!r} in the last {len(recent)} sessions. "
        f"Raise --search-limit to look further back."
    )


def _as_dict(workout: Workout) -> dict:
    """Flatten a workout for --json output."""
    return {
        "id": workout.id,
        "title": workout.title,
        "routine_id": workout.routine_id,
        "start_time": workout.start_time,
        "end_time": workout.end_time,
        "duration_seconds": workout.duration_seconds,
        "total_sets": workout.total_sets,
        "total_reps": workout.total_reps,
        "total_volume_kg": workout.total_volume_kg,
        "exercises": [
            {
                "index": e.index,
                "title": e.title,
                "notes": e.notes,
                "exercise_template_id": e.template_id,
                "sets": [
                    {
                        "type": s.type,
                        "weight_kg": s.weight_kg,
                        "reps": s.reps,
                        "distance_meters": s.distance_meters,
                        "duration_seconds": s.duration_seconds,
                        "rpe": s.rpe,
                    }
                    for s in e.sets
                ],
            }
            for e in workout.exercises
        ],
    }


@app.command("list")
def list_workouts(
    limit: int = typer.Option(10, "--limit", "-n", help="How many to show."),
    routine: str = typer.Option(
        None, "--routine", "-r", help="Only show workouts whose title matches."
    ),
    json_output: bool = typer.Option(
        False, "--json", help="Emit JSON instead of a table."
    ),
) -> None:
    """List recent workouts, newest first."""
    with HevyClient() as client:
        # Filtering happens client-side, so scan wider when a filter is set.
        fetch = max(limit, DEFAULT_SEARCH_LIMIT) if routine else limit
        raw = client.list_workouts(limit=fetch)

    workouts = [Workout.from_api(w) for w in raw]
    if routine:
        workouts = [w for w in workouts if _matches_routine(w, routine)][:limit]

    logger.info("Fetched %d workouts", len(workouts))

    if json_output:
        console.print_json(json.dumps([_as_dict(w) for w in workouts]))
        return

    if not workouts:
        console.print("[yellow]No matching workouts.[/yellow]")
        return

    table = Table(title=f"Recent workouts ({len(workouts)})", title_justify="left")
    table.add_column("Date")
    table.add_column("Workout")
    table.add_column("Time", justify="right")
    table.add_column("Ex", justify="right")
    table.add_column("Sets", justify="right")
    table.add_column("Volume", justify="right")
    table.add_column("Id", style="dim")

    for workout in workouts:
        started = workout.started
        table.add_row(
            started.strftime("%Y-%m-%d %H:%M") if started else "-",
            workout.title,
            format_duration(workout.duration_seconds),
            str(len(workout.exercises)),
            str(workout.total_sets),
            f"{format_number(workout.total_volume_kg)} kg",
            workout.id.split("-")[0],
        )

    console.print(table)


@app.command("show")
def show_workout(
    workout_id: str = typer.Argument(
        None, help="Workout id. Defaults to the most recent workout."
    ),
    routine: str = typer.Option(
        None,
        "--routine",
        "-r",
        help="Show the latest workout whose title matches this routine.",
    ),
    search_limit: int = typer.Option(
        DEFAULT_SEARCH_LIMIT,
        "--search-limit",
        help="How many recent workouts to scan when resolving --routine.",
    ),
    last: bool = typer.Option(
        False, "--last", help="Show the most recent workout (the default)."
    ),
    json_output: bool = typer.Option(
        False, "--json", help="Emit JSON instead of a table."
    ),
) -> None:
    """
    Show every set of a single workout.

    With no arguments this shows your most recent session; --routine picks the
    latest session logged against a given routine.
    """
    if workout_id and routine:
        raise typer.BadParameter("Pass a workout id or --routine, not both.")

    with HevyClient() as client:
        if workout_id:
            workout = Workout.from_api(client.get_workout(workout_id))
        else:
            # --last is the default behaviour, so it needs no branch of its own.
            found = _find_workout(client, routine, search_limit)
            workout = Workout.from_api(client.get_workout(found.id))

    if json_output:
        console.print_json(json.dumps(_as_dict(workout)))
        return

    started = workout.started
    console.print(
        f"\n[bold]{workout.title}[/bold] "
        f"[dim]{workout.id}[/dim]\n"
        f"{started.strftime('%a %d %b %Y, %H:%M') if started else 'unknown start'} "
        f"· [cyan]{format_duration(workout.duration_seconds)}[/cyan]"
    )
    if workout.description:
        console.print(f"[dim]{workout.description}[/dim]")

    table = Table(box=None, pad_edge=False, show_header=False)
    table.add_column("#", justify="right", style="dim")
    table.add_column("Exercise")
    table.add_column("Sets")

    for exercise in workout.exercises:
        sets = "   ".join(s.describe() for s in exercise.sets)
        table.add_row(str(exercise.index + 1), exercise.title, sets)
        if exercise.notes:
            table.add_row("", "", f"[dim]{exercise.notes}[/dim]")

    console.print(table)
    console.print(
        f"\n[dim]{len(workout.exercises)} exercises · {workout.total_sets} sets · "
        f"{workout.total_reps} reps · "
        f"{format_number(workout.total_volume_kg)} kg volume[/dim]\n"
    )
