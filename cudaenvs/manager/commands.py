import click


@click.command()
@click.option('--env-name', '-n', type=str, default=None)
def template(env_name):
    click.echo('template')

@click.command()
@click.option('--env-name', '-n', type=str, default=None)
def build(env_name):
    click.echo('build')


@click.command()
@click.option('--env-name', '-n', type=str, default=None)
def play(env_name):
    click.echo('play')


@click.command()
@click.option('--env-name', '-n', type=str, default=None)
def stop(env_name):
    click.echo('stop')


@click.command()
@click.option('--env-name', '-n', type=str, default=None)
def clean(env_name):
    click.echo('clean')
