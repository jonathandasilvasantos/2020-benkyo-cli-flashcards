import click
from ..utils.config import read_config
from ..model.card import Card, castcard
from ..view.cardview import UICard
from ..view.model.uicardstate import UICardState
from ..view.model.uicarddata import UICardData
from ..view.model.uicardshortcut import UICardShortcut
from prompt_toolkit.application import get_app
from ..view.widgets.uicardtoolbar import UICardToolbar, get_toolbar
from ..view.widgets.uicardbutton import UICardButton


@click.command()
def pratice():
    startui(castcard()[0])



def startui(card):

    pratice_toolbar = UICardToolbar('pratice', 'pratice', [
    UICardButton('Next', next),
    UICardButton('Reveal', reveal),
    UICardButton('Quit', exit_)
    ])

    pratice_reveled_toolbar = UICardToolbar('pratice_reveled', 'pratice_reveled', [
    UICardButton('Next', next),
    UICardButton('Quit', exit_)
    ])

    edit_toolbar = UICardToolbar('edit', 'edit', [
    UICardButton('Save', save),
    UICardButton('Cancel', cancel),
    UICardButton('Quit', exit_)
    ])

    shortcuts = [
        UICardShortcut('edit', 'c-e', edit_shortcut),
        UICardShortcut('save', 'c-s', save),
        UICardShortcut('next', 'c-n', next),
        UICardShortcut('revel', 'c-r', reveal),
        UICardShortcut('cancel', 'escape', cancel)
    ]


    uicard_data = UICardData(card.id, card.frontal, card.hidden, card.tag)
    uicard_state = UICardState([pratice_toolbar, pratice_reveled_toolbar, edit_toolbar], mode='pratice', shortcuts=shortcuts)
    uicard = UICard(uicard_data, uicard_state, None)

    app = uicard.create_app()
    app.run()



def edit_shortcut(event):
    UICard().change_mode('edit')
    UICard().layout.focus(UICard().frontal_buffer)

    UICard().uicard_state.frontal_editable = True
    if UICard().uicard_state.show_hidden == True: UICard().uicard_state.hidden_editable = True
    UICard().uicard_state.tag_editable = True


def save(event=None):
    if UICard().uicard_state.mode != 'edit': return
    card = Card.select().where(Card.id == UICard().uicard_data.id)[0]

    card.frontal = UICard().frontal_buffer.text
    card.hidden = UICard().hidden_buffer.text
    card.tag = UICard().tag_buffer.text
    card.save()
    UICard().uicard_data = UICardData(card.id, card.frontal, card.hidden, card.tag)

    UICard().uicard_state.frontal_editable = False
    UICard().uicard_state.hidden_editable = False
    UICard().uicard_state.tag_editable = False
    if UICard().uicard_state.show_hidden:
        UICard().change_mode('pratice_reveled')
    else:
        UICard().change_mode('pratice')



def cancel(event=None):
    if UICard().uicard_state.mode != 'edit': return
    UICard().uicard_state.frontal_editable = False
    UICard().uicard_state.hidden_editable = False
    UICard().uicard_state.tag_editable = False
    UICard().frontal_buffer.text = UICard().uicard_data.frontal
    UICard().hidden_buffer.text = UICard().uicard_data.hidden
    UICard().tag_buffer.text = UICard().uicard_data.tag
    if UICard().uicard_state.show_hidden:
        UICard().change_mode('pratice_reveled')
    else:
        UICard().change_mode('pratice')


def exit_():
    get_app().exit()
    exit(0)
def reveal(event=None):
    if UICard().uicard_state.mode != 'pratice': return
    if UICard().uicard_state.show_hidden == False:
        card = Card.select().where(Card.id == UICard().uicard_data.id)[0]
        card.penality()
    UICard().uicard_state.show_hidden = True
    UICard().hidden_buffer.text = UICard().uicard_data.hidden
    first_button = get_toolbar(UICard().uicard_state.toolbars, UICard().uicard_state.mode).prompt_buttons[0]
    UICard().change_mode('pratice_reveled')

def next(event=None):
    if (UICard().uicard_state.mode != 'pratice') and (UICard().uicard_state.mode != 'pratice_reveled'): return
    if UICard().uicard_state.show_hidden == False:
        card = Card.select().where(Card.id == UICard().uicard_data.id)[0]
        card.reward()


    card = castcard()[0]
    uicard_data = UICardData(card.id, card.frontal, card.hidden, card.tag)
    UICard().uicard_data = uicard_data
    UICard().uicard_state.show_hidden = False
    UICard().change_mode('pratice')
