import click
from ..model.card import Card

@click.command()
@click.option('--cardid', '-id', type=click.INT, default=-1, help='Specify a card to be removed')
@click.option('--front', '-f', default='', type=click.STRING, help='Frontal face')
@click.option('--hidden', '-hf', default='', type=click.STRING, help='Hidden face')
@click.option('--tag', '-t', default='', type=click.STRING, help='TAG')
def edit(cardid, front, hidden, tag):

    cards = Card.select().where(Card.id == cardid)
    for entry in cards:
        if len(front) > 0:
            entry.frontal = front
            click.echo('Frontal face updated.')
        if len(hidden) > 0:
            entry.hidden = hidden
            click.echo('Hidden face updated.')
        if len(tag) > 0:
            entry.tag = tag
            click.echo('TAG updated.')

        entry.save()
