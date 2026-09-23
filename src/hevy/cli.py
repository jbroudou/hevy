"""Command line entry point for hevy."""

import sys

import typer
from rich.console import Console

from . import __version__
from .api import HevyAPIError
from .commands import routines, workouts
from .config import ConfigError, config
from .logger import logger

app = typer.Typer(
    help="Manage your Hevy workouts and routines.",
    invoke_without_command=True,
    add_completion=False,
)
app.add_typer(routines.app, name="routines")
app.add_typer(workouts.app, name="workouts")

err_console = Console(stderr=True)


@app.callback()
def main(
    ctx: typer.Context,
    version: bool = typer.Option(
        False, "--version", help="Show the version and exit.", is_eager=True
    ),
) -> None:
    """Manage your Hevy workouts and routines."""
    if version:
        typer.echo(f"hevy {__version__}")
        raise typer.Exit()
    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())
        raise typer.Exit()
    config.validate()


def run() -> None:
    """Entry point wrapper that turns known failures into clean messages."""
    try:
        app()
    except ConfigError as exc:
        err_console.print(f"[red]Configuration error:[/red] {exc}")
        sys.exit(2)
    except HevyAPIError as exc:
        logger.error("API call failed: %s", exc)
        if exc.status_code == 401:
            err_console.print(
                "[red]Unauthorized:[/red] check HEVY_API_KEY in your .env file."
            )
        else:
            err_console.print(f"[red]{exc}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    run()
