from random import shuffle
import math
import players
import config

"""define the card ranks and suits
   the value of Ace, Jack, King and Queen are defined in config.py
"""
ranks = {'Two': 2,
         'Three': 3,
         'Four': 4,
         'Five': 5,
         'Six': 6,
         'Seven': 7,
         'Eight': 8,
         'Nine': 9,
         'Ten': 10,
         'Jack': config.Default.JACK_VALUE,
         'Queen': config.Default.QUEEN_VALUE,
         'King': config.Default.KING_VALUE,
         'Ace': config.Default.ACE_VALUE
        }
suits = ['Spade', 'Heart', 'Diamond', 'Club']

# make a deck by the defined ranks and suits in a tuple of (rank, suit)
def make_deck():
    return [[rank, suit] for rank in list(ranks.keys()) for suit in suits]

deck = []
# find the number of deck needed; max 3 players for each deck
deck_number = math.ceil(players.players_number / 3)
# make a combination of decks
for _ in range(0, deck_number):
    deck += make_deck()

# shuffle deck(s) to be sure that it is randomley arranged
shuffle(deck)
print('\n\n====================================================\n')
print(len(deck))
print(deck)
print('\n====================================================\n\n')

# add co-values to the dictionary
ranks['Ace11'] = 11
ranks['Ace1'] = 1
