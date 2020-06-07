import numpy as np
import peewee
from utils.access import get_database
from utils.config import read_config
from numpy.random import choice

class Card(peewee.Model):
    frontal = peewee.TextField()
    hidden = peewee.TextField()
    tag = peewee.CharField()
    score = peewee.IntegerField(default=100)
    level = peewee.IntegerField(default=0)
    phase = peewee.IntegerField(default=0)
    last = peewee.TimestampField()
    next = peewee.TimestampField()

    class Meta:
        database = get_database()
        db_table = 'cards'

    def reward(self):
        self.score = self.score - (self.score * read_config('benkyo_reward'))
        self.save()

    def penality(self):
        self.score = self.score + (self.score * read_config('benkyo_penality'))
        self.save()


def scores(cards):
    p = []
    for entry in cards:
        p.append(entry.score)
    return p

def castcard(count=1, tag=None, replace=True):
    cards = Card.select()
    if tag is not None:
        cards = cards.where(tag == tag)
    cards = choice(cards, count, scores(cards))
    return cards
