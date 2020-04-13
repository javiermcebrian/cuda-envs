import click
import json
from pathlib import Path
from typing import Union

from ..environment import Environment


@click.command()
@click.option('--updates_fn', '-i', type=Path, required=True)
def update(updates_fn):
    Environment().update(updates_fn=updates_fn)
    click.echo('Config updated')


@click.command()
@click.option('--default', '-d', is_flag=True)
@click.option('--keys', '-k', multiple=True, type=click.STRING, default=None)
def remove(default, keys):
    click.echo(Environment().remove(is_default=default, keys=keys))


@click.command()
def list():
    click.echo(Environment().list())


@click.command()
def dump():
    click.echo(Environment().dump())
