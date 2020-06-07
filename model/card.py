import numpy as np
import peewee
from utils.access import get_database
from utils.config import read_config
from numpy.random import choice
from numpy import min, max
import numpy as np

class Card(peewee.Model):
    frontal = peewee.TextField()
    hidden = peewee.TextField()
    tag = peewee.CharField()
    score = peewee.FloatField(default=100)
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
    A = []
    for entry in cards:
        A.append(entry.score)
    s = np.sum(A)
    P = []
    for index, entry in enumerate(A):
        r = (entry * 100) / s
        P.append(r/100)
    return P




    print(np.sum(np.array(A)))
    A = (A-np.min(A))/(np.max(A)-np.min(A))
    print(A)
    exit(0)
    return A

def castcard(count=1, tag=None, replace=True):
    cards = Card.select()
    if tag is not None:
        cards = cards.where(tag == tag)

    for c in cards:
        pass
    #exit(0)



    selected = choice(cards, count, p = scores(cards) )

    return selected
