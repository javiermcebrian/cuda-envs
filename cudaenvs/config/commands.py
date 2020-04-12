import click
import json
from pathlib import Path
from typing import Union

from ..placeholders import Zoo


@click.command()
@click.option('--items_fn', '-i', type=Path, required=True)
def update(items_fn):
    """
    read files, check default keys, update default, check envs keys, check completeness with new default, update file
    # Keys from: user, volume, environment
    """
    click.echo('update')


@click.command()
@click.option('--default', '-d', is_flag=True)
@click.option('--keys', '-k', multiple=True, type=click.STRING, default=None)
def remove(default, keys):
    click.echo(Zoo().remove(is_default=default, keys=keys))


@click.command()
def dump():
    click.echo(Zoo().dump())
