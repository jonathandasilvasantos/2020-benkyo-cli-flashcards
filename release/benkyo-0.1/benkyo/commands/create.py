import click
import os
from ..model.card import Card
from ..utils.config import read_config
from ..utils.validate import is_repository_avaliable

@click.command()
@click.argument('path')
def create(path):
    if os.path.isfile(path):
        click.echo('Ops! You are passing a file path! We need a valid directory path.')
        exit(1)
    if not os.path.isdir(path):
        click.echo("Ops! It's not a valid path!")
        exit(1)

    benkyo_folder_name = read_config('benkyo_repository_folder_name')
    repository_path = os.path.join(path, benkyo_folder_name)

    if os.path.isdir(repository_path):
        click.echo('Ops! Maybe you already have a flashcard repository inside this path')
        exit(1)
    if os.path.isfile(repository_path):
        click.echo('Check the file: ' + repository_path)
        exit(1)


    click.echo('Creating a new flashcard repository in '+ path)
    os.mkdir(repository_path)
    database_path = os.path.join(repository_path, read_config('benkyo_database_filename'))

    Card.create_table()

    if is_repository_avaliable():
        click.echo('Repository successfully created!')
