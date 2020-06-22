import click
from ..commands.version import version
from ..commands.create import create
from ..commands.add import add
from ..commands.list import list
from ..commands.remove import remove
from ..commands.edit import edit
from ..commands.importcsv import importcsv
from ..commands.pratice import pratice

@click.group()
def cli():
    pass

cli.add_command(version)
cli.add_command(create)
cli.add_command(remove)
cli.add_command(add)
cli.add_command(importcsv)
cli.add_command(list)
cli.add_command(edit)
cli.add_command(pratice)



if __name__ == '__main__':
    cli()
