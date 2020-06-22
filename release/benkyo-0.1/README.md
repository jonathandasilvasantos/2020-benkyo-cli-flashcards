# Benkyo

## What is it?
Benkyo is a learning tool using flashcards created to work initially only in console mode on the terminal.
Benkyo means 'to study' in Japanese. Or is that a joke?

## Installation
Use pip to install benkyo:
> pip3 install https://github.com/jonathandasilvasantos/2020-benkyo-cli-flashcards/raw/master/release/benkyo-0.1-py3-none-any.whl

## How to use it?

First, lets create a folder to keep our flashcards
> mkdir my_flashcards
> cd my_flashcards
>
Now we need to create a flashcards repository.
> benkyo create .

Ok! Now we have a flashcards repository.
Lets download a CSV file with some cards:
> curl -O https://raw.githubusercontent.com/jonathandasilvasantos/2020-benkyo-cli-flashcards/master/examples/french.csv

Nice, we have a repository and a CSV file with cards. Now we can import the cards to our repository with the following command:
> benkyo importcsv french.csv

Great! Now we everthing is ready and we can reviw these cards with the following command:
> benkyo pratice
