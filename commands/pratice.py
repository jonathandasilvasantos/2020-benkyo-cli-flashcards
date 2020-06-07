import click
from utils.config import read_config
from model.card import Card, castcard
from view.cardview import UICardData, UICardState, UICardCallbacks, UICardButton, UICard

from prompt_toolkit.application import get_app


@click.command()
def pratice():
    startui(castcard()[0])



def startui(card):

    buttons = [ UICardButton('Next', next), UICardButton('Reveal', reveal), UICardButton('Quit', exit_)]


    uicard_data = UICardData(card.id, card.frontal, card.hidden, card.tag)
    uicard_state = UICardState(buttons)
    uicard = UICard(uicard_data, uicard_state, None)




    app = uicard.create_app()
    app.run()



def exit_():
    get_app().exit()
    exit(0)
def reveal():
    UICard().uicard_state.show_hidden = True

def next():
    card = Card.select().where(Card.id == UICard().uicard_data.id)[0]
    card.reward()


    card = castcard()[0]
    uicard_data = UICardData(card.id, card.frontal, card.hidden, card.tag)
    UICard().uicard_data = uicard_data
    UICard().uicard_state.show_hidden = False
