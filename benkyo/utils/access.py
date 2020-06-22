import peewee
import os

from ..utils.config import read_config

def get_database():
    cwd = os.getcwd()
    path = os.path.join(cwd, read_config('benkyo_repository_folder_name'))
    database_path = os.path.join(path, read_config('benkyo_database_filename'))
    db = peewee.SqliteDatabase(database_path)
    return db
