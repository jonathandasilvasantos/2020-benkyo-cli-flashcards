import click
from ..model.card import Card
import peewee



@click.command()
@click.argument('removeall', default='', type=click.STRING, required=False)
@click.option('--cardid', '-id', type=click.INT, default=-1, help='Specify a card to be removed')
@click.option('--tag', '-t', type=click.STRING, default='', help='Remove all cards of a TAG')
def remove(removeall, cardid, tag):

    all = False
    if removeall == 'all': all = True

    if (cardid == -1) and (len(tag) < 1) and (all == False):
        click.echo("Ops! You need to specify a card id or a tag to execute this command!")
        exit(1)

    query = ''
    if cardid != -1:
        query = Card.delete().where(Card.id == cardid)
    if len(tag) > 0:
        query = Card.delete().where(Card.tag == tag)

    if all:
        click.confirm('Are you sure that you want to remove all cards?', abort=True)
        query = Card.delete()

    result = query.execute()
    click.echo(str(result) + ' card(s) removed.')
