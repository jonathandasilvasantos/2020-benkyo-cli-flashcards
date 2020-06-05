import click
from model.card import Card, scores
from view.cardview import UICardData, UICardState, UICardCallbacks, UICardButton, UICard
from numpy.random import choice
from prompt_toolkit.application import get_app

@click.command()
def pratice():


    cards = Card.select()
    cards = choice(cards, 1, scores(cards))

    for entry in cards:
        startui(entry)


def next():
    pass

def reveal():
    pass

def startui(card):

    buttons = [ UICardButton('Next'), UICardButton('Reveal'), UICardButton('Quit', exit_)]


    uicard_data = UICardData(card.frontal, card.hidden, card.tag)
    uicard_state = UICardState(buttons)
    uicard = UICard(uicard_data, uicard_state, None)

    app = uicard.create_app()
    app.run()

def exit_():
    get_app().exit()
    exit(0)
