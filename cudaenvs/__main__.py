import click
from pathlib import Path
import json

from .config.commands import update, remove, dump
from .manager.commands import template, build, play, stop, clean


@click.group()
def cli():
    pass


@click.group()
def config():
    pass


# Config commands
config.add_command(update)
config.add_command(remove)
config.add_command(dump)

# Manager commands
cli.add_command(config)
cli.add_command(template)
cli.add_command(build)
cli.add_command(play)
cli.add_command(stop)
cli.add_command(clean)


if __name__ == '__main__':
    cli()
