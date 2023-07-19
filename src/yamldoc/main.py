import pathlib
import sys

import click


@click.command(name="yamldoc")
@click.option(
    "--out",
    type=click.File(mode="w"),
    help="File to write to.",
    default=sys.stdout,
    show_default="STDOUT",
)
@click.argument("schema", required=True, type=click.Path(exists=True, dir_okay=False, path_type=pathlib.Path))
def cmd(out, schema):
    pass
