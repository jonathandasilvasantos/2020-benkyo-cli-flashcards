import click
import os
from ..model.card import Card
from ..utils.validate import assert_repository_is_avaliable
from ..utils.config import read_config
from subprocess import call
import sys


@click.command()
@click.option('--front', '-f', prompt='Frontal Face', help='Frontal Face of the new card.', required=True)
@click.option('--hidden', '-hf', prompt='Hidden Face', help='Hidden face of the new card.', required=True)
@click.option('--tag', '-t', default='default', prompt='TAG', help='TAG of the new card.', required=False)
@click.option('--count', '-c', required=False, type=click.INT, default=1, help='How many entries. Set -1 to add entries withou a prefedined limit.')
def add(front, hidden, tag, count):
    assert_repository_is_avaliable()

    card = Card()
    card.frontal = front
    card.hidden = hidden
    card.tag = tag
    card.save()

    if (count > 1) or (count < 0):
        if count < 0:
            click.confirm('Do you want to continue?', abort=True)
        cmdline = [read_config('python_interpreter'), sys.argv[0], 'add', '-c', str(count-1) ]
        call(cmdline)
