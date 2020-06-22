import click
import os
from ..utils.config import read_config

def is_repository_avaliable():
    cwd = os.getcwd()
    path = os.path.join(cwd, read_config('benkyo_repository_folder_name'))
    if os.path.isfile(path):
        click.echo("Ops! Why "+ path + " is a file? I expected to found a directory!")
        exit(1)
    if os.path.isdir(path):
        path_database = os.path.join(path, read_config('benkyo_database_filename'))
        if os.path.isfile(path_database):
            return True
    return False

def assert_repository_is_avaliable():
    if not is_repository_avaliable():
        click.echo("Ops! First you need to create a repository using 'create' command.")
        exit(1)
