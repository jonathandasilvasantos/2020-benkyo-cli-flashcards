import os
import csv
import click
from ..model.card import Card

@click.command()
@click.argument('path')
@click.option('--frontalcol', '-fc', type=click.INT, default=0, help='Column index of Frontal Face')
@click.option('--hiddencol', '-hfc', type=click.INT, default=1, help='Column index of Hidden Face')
@click.option('--tagcol', '-tc', type=click.INT, default=2, help='Column index of TAG')
@click.option('--delimiter', type=click.STRING, default=',', help='CSV column delimiter character.')
@click.option('--header', type=click.BOOL, default=False, help='Header (False by default)')
def importcsv(path, frontalcol, hiddencol, tagcol, delimiter, header):
    if not os.path.isfile(path):

        exit(1)

    entries = 0
    with open(path, 'r') as csvinput:
        csvreader = csv.reader(csvinput, delimiter=delimiter)
        for index, row in enumerate(csvreader):
            if header and (index == 0): continue
            card = Card()
            card.frontal = row[frontalcol]
            card.hidden = row[hiddencol]
            try:
                card.tag = row[tagcol]
            except:
                card.tag = 'default'
            card.save()
            entries = entries + 1


    click.echo(str(entries) + ' card(s) imported')
