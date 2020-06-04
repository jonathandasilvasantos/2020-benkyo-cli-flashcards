import click
from model.card import Card, scores
from numpy.random import choice
import curses
import traceback
from utils.ui import initscreen, releasescreen

@click.command()
def pratice():


    cards = Card.select()
    cards = choice(cards, 1, scores(cards))

    for entry in cards:
        startui(entry)


def startui(card):

    k = 0

    def refresh(stdscr):
        stdscr.clear()
        stdscr.border(0)
        stdscr.addstr(5, 5, card.frontal, curses.A_BOLD)
        stdscr.addstr(7, 5, 'Press q to close this screen', curses.A_NORMAL)
        stdscr.addstr(8, 5, str(k), curses.A_NORMAL)




    try:
        stdscr = initscreen()
        refresh(stdscr)
        while True:
            refresh(stdscr)
            k = stdscr.getch()
            if k == ord('q'):
                break

    except:
        traceback.print_exc()     # print trace back log of the error
    finally:
        releasescreen(stdscr)
