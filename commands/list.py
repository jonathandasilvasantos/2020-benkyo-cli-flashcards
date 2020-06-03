import click
import peewee
from model.card import Card


@click.command()
@click.option('--tag', '-t', default='', type=click.STRING, help='Filter the list with a TAG.')
def list(tag):

    cards = Card.select()
    if len(tag) > 0:
        cards = cards.where(Card.tag == tag)
    for entry in cards:
        print( str(entry.id) + "   tag: " + entry.tag)
        print(entry.frontal)
        print(entry.hidden + '\n')
