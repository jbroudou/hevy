"""`hevy routines` commands."""

import json
from pathlib import Path

import typer
from rich.console import Console
from rich.tree import Tree

from ..api import HevyClient, unwrap_routine
from ..logger import logger
from ..models import group_routines_by_folder
from ..spec import build_routine_payload

app = typer.Typer(help="Inspect your Hevy routines.")
console = Console()


@app.command("list")
def list_routines(
    json_output: bool = typer.Option(
        False, "--json", help="Emit JSON instead of a tree."
    ),
    empty: bool = typer.Option(
        True, "--empty/--no-empty", help="Include folders that hold no routines."
    ),
) -> None:
    """List all routines grouped by their folder."""
    with HevyClient() as client:
        folders = client.list_routine_folders()
        routines = client.list_routines()

    logger.info("Fetched %d folders and %d routines", len(folders), len(routines))
    grouped = group_routines_by_folder(folders, routines)

    if not empty:
        grouped = [f for f in grouped if f.routines]

    if json_output:
        payload = [
            {
                "id": f.id,
                "title": f.title,
                "index": f.index,
                "routines": [
                    {
                        "id": r.id,
                        "title": r.title,
                        "exercise_count": r.exercise_count,
                        "updated_at": r.updated_at,
                    }
                    for r in f.routines
                ],
            }
            for f in grouped
        ]
        console.print_json(json.dumps(payload))
        return

    tree = Tree(f"[bold]Routines[/bold] ([cyan]{len(routines)}[/cyan] total)")
    for folder in grouped:
        label = (
            f"[bold yellow]{folder.title}[/bold yellow] "
            f"[dim]({len(folder.routines)})[/dim]"
        )
        branch = tree.add(label)
        if not folder.routines:
            branch.add("[dim]empty[/dim]")
            continue
        for routine in folder.routines:
            plural = "exercise" if routine.exercise_count == 1 else "exercises"
            branch.add(
                f"{routine.title} "
                f"[dim]— {routine.exercise_count} {plural} · {routine.id}[/dim]"
            )

    console.print(tree)


@app.command("create")
def create_routine(
    spec_file: Path = typer.Argument(
        ..., exists=True, dir_okay=False, help="Path to a routine spec JSON file."
    ),
    dry_run: bool = typer.Option(
        False, "--dry-run", help="Show what would be sent without writing anything."
    ),
) -> None:
    """
    Create a routine from a spec file.

    Missing custom exercise templates named in the spec are created first.
    Neither routines nor templates can be deleted through the Hevy API, so
    preview with --dry-run before committing.
    """
    from ..spec import load_spec

    spec = load_spec(spec_file)

    with HevyClient() as client:
        payload, created = build_routine_payload(
            client, spec, create_missing=not dry_run
        )

        if dry_run:
            console.print_json(json.dumps(payload))
            console.print(
                f"\n[yellow]Dry run.[/yellow] Would create "
                f"[bold]{len(created)}[/bold] custom template(s): "
                f"{', '.join(created) or 'none'}"
            )
            console.print(
                f"Would create routine [bold]{payload['title']}[/bold] "
                f"in folder_id [bold]{payload['folder_id']}[/bold] "
                f"with [bold]{len(payload['exercises'])}[/bold] exercises."
            )
            return

        response = client.create_routine(payload)

    routine = unwrap_routine(response)
    logger.info("Created routine %s", routine.get("id"))

    for title in created:
        console.print(f"[green]Created template[/green] {title}")
    console.print(
        f"[green]Created routine[/green] [bold]{routine.get('title')}[/bold] "
        f"[dim]{routine.get('id')}[/dim]"
    )


@app.command("update")
def update_routine(
    spec_file: Path = typer.Argument(
        ..., exists=True, dir_okay=False, help="Path to a routine spec JSON file."
    ),
    dry_run: bool = typer.Option(
        False, "--dry-run", help="Show what would be sent without writing anything."
    ),
) -> None:
    """
    Overwrite an existing routine from its spec file.

    The spec must carry the routine's `routine_id`. Every exercise, set and
    note in the routine is replaced, so edits made in the app are lost.
    """
    from ..spec import load_spec

    spec = load_spec(spec_file)
    routine_id = spec.get("routine_id")
    if not routine_id:
        console.print(f"[red]{spec_file} has no routine_id.[/red] Create it first.")
        raise typer.Exit(2)

    with HevyClient() as client:
        payload, created = build_routine_payload(
            client, spec, create_missing=not dry_run
        )

        if dry_run:
            console.print_json(json.dumps(payload))
            console.print(
                f"\n[yellow]Dry run.[/yellow] Would overwrite routine "
                f"[bold]{routine_id}[/bold] with "
                f"[bold]{len(payload['exercises'])}[/bold] exercises."
            )
            return

        response = client.update_routine(routine_id, payload)

    routine = unwrap_routine(response)
    logger.info("Updated routine %s", routine_id)
    for title in created:
        console.print(f"[green]Created template[/green] {title}")
    title = routine.get("title", spec["title"])
    console.print(
        f"[green]Updated routine[/green] [bold]{title}[/bold] [dim]{routine_id}[/dim]"
    )
