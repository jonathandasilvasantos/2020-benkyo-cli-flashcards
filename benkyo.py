import click
from commands.version import version
from commands.create import create
from commands.add import add

@click.group()
def cli():
    pass

cli.add_command(version)
cli.add_command(create)
cli.add_command(add)



if __name__ == '__main__':
    cli()
