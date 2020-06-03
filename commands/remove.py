import click
from model.card import Card
import peewee


@click.command()
@click.option('--cardid', '-id', type=click.INT, default=-1, help='Specify a card to be removed')
@click.option('--tag', '-t', type=click.STRING, default='', help='Remove all cards of a TAG')
def remove(cardid, tag):

    if (cardid == -1) and (len(tag) < 1):
        click.echo("Ops! You need to specify a card id or a tag to execute this command!")
        exit(1)

    query = ''
    if cardid != -1:
        query = Card.delete().where(Card.id == cardid)
    if len(tag) > 0:
        query = Card.delete().where(Card.tag == tag)

    result = query.execute()
    click.echo(str(result) + ' card(s) deleted.')
