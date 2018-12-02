from random import shuffle
from colored import fg, bg, attr
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
suits = ['♠', '♥', '♦', '♣']


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

# add co-values to the dictionary
ranks['Ace11'] = 11
ranks['Ace1'] = 1


def print_card(card, Flag):
    # define the color of the card
    if card[1] in ['♠', '♣']:
        k = 0
    else:
        k = 1
    # define how to show the value of the cards
    if card[0] == 'Jack':
        card_value = 'J '
    elif card[0] == 'Queen':
        card_value = 'Q '
    elif card[0] == 'King':
        card_value = 'K '
    elif card[0] == 'Ten':
        card_value = '10'
    elif card[0] in ['Ace', 'Ace1', 'Ace11']:
        card_value = 'A '
    else:
        card_value = str(ranks[card[0]]) + ' '

    if Flag == 'Print':
        print('\t {}{} {} {} {} '.format(fg(k), bg(15), card_value, card[1],
                                         attr(0)))
    else:
        return str(card_value) + ' ' + str(card[1])


def print_sum(player_sum):
    if player_sum < 10:
        space = 4 * ' '
    else:
        space = 3 * ' '
    print(' {}{}{}  SUM:   {}{}{}\n'.format(attr(1), fg(22), bg(15),
                                            player_sum, space, attr(0)))
