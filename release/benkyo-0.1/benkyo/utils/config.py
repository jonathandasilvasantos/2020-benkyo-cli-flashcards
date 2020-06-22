import os
from ..consts import consts

def read_config(keyname):
    result = ''
    try:
        result = os.environ[keyname.upper()]
    except KeyError as e:
        result = consts.entries[keyname]
    return result
