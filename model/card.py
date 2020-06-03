import peewee
from utils.access import get_database

class Card(peewee.Model):
    frontal = peewee.TextField()
    hidden = peewee.TextField()
    tag = peewee.CharField()
    score = peewee.IntegerField(default=0)
    level = peewee.IntegerField(default=0)
    phase = peewee.IntegerField(default=0)
    last = peewee.TimestampField()
    next = peewee.TimestampField()

    class Meta:
        database = get_database()
        db_table = 'cards'
