import deck
import players
from input import get_text as get_text
from input import get_number as get_number
import config


play = {}

status = ['Stand', 'Hit', 'Bust', 'Split']


def bet(player_name, previous_bet):
    # define the messages; change them in config.py
    input_txt = config.Messages.BET_INPUT_TXT
    success_msg = config.Messages.BET_SUCCESS_TXT
    error_msg1 = config.Messages.BET_ERROR_TXT1
    error_msg2 = config.Messages.ERROR_TXT
    # set the new bet
    return get_number('Bet', player_name, input_txt, success_msg,
                      error_msg1, error_msg2, previous_bet)


# ask the desired value of Ace from the user
def is_ace(player_name, player, key, ace_type):
    if player[key][0][0] == ace_type:
        input_txt = config.Messages.ACE_INPUT_TXT
        success_msg = config.Messages.ACE_SUCCESS_TXT
        error_msg1 = config.Messages.ACE_ERROR_TXT
        error_msg2 = config.Messages.ERROR_TXT
        bet = 0
        player[key][0][0] = get_number('Ace', player_name, input_txt,
                                       success_msg, error_msg1, error_msg2,
                                       bet)


# sum up the value of cards
def sum_up(player_name, player):
    sum_value = 0
    for key in list(player.keys()):
        if key == 'sum':
            continue
        sum_value += deck.ranks[player[key][0][0]]
    return sum_value


# get the second, third and more card for each player
def play_game(player, j, Flag):
    play[player]['sum'] = sum_up(player, play[player])
    while play[player]['sum'] <= 21 and \
          play[player][j-1][2] == 'Hit':

        if Flag == 'init' and j > 2:
            break

        print(j, Flag, play[player])

        print('\n ********************* p: {} ******* j: {}'.format(player, j))
        print('\nplay_init:\n', play[player])

        # initiate the round
        play[player][j] = [None, 0, None]

        # get a new card
        play[player][j][0] = deck.deck.pop()
        print('\n\n::::::::::::::::::>>> ', play[player][j][0])
        is_ace(player, play[player], j, 'Ace')

        # checks if split is eligible
        if j == 2 and \
           player[-3:-1] != '__' and \
           play[player][1][0][0] == play[player][2][0][0]:

            # ask the user if she wants to split
            input_txt = config.Messages.CHOICE_TYPE_TXT2
            error_msg = config.Messages.CHOICE_ERROR_TXT
            answer = get_text(player, input_txt, error_msg,
                              ['y', 'yes', 'n', 'no'])
            # create two hands for the player and remove the old one
            if answer.lower() in ['y', 'yes']:

                # create the first part of the splited hand
                play[player + '__1'] = play[player]
                play[player + '__1'].pop(2)

                # create the second part of the splited hand
                play[player + '__2'] = play[player + '__1']
                play[player + '__2'][1][0] = play[player][1][0]

                # update sum
                play[player + '__1']['sum'] = int(play[player]['sum'] / 2)
                play[player + '__2']['sum'] = int(play[player]['sum'] / 2)

                # delete the old hand
                play.pop(player)

                """ update the list of names
                    it doesn't remove the old name from the list,
                    it will be removed later in the calling loop.
                """
                k = players.players_name.index(player)
                players.players_name.insert(k + 1, player + '__1')
                players.players_name.insert(k + 2, player + '__2')
                break

        # check if the hand is 21
        play[player]['sum'] = sum_up(player, play[player])
        if play[player]['sum'] == 21:
            print('---SUM---: ', play[player]['sum'])

            # update the bet of the new round as the previous one
            play[player][j][1] = play[player][j-1][1]
            print(config.Messages.WON_TXT.format(player, play[player][j-1][1]))
            break

        """if it's Dealer's turn, there are some rules:
           The Dealer must hit when it has a total of 16 points or less
           and must stand with a total of 17 points or more.
        """
        play['Dealer']['sum'] = sum_up('Dealer', play['Dealer'])
        if player == 'Dealer' and play['Dealer']['sum'] <= 16:
            play[player][j][2] = 'Hit'
            continue
        elif player == 'Dealer' and play['Dealer']['sum'] >= 17:
            play[player][j][2] = 'Stand'
            break

        # if the player is not the Dealer
        if j == 1:
            play[player][j][2] = 'Hit'
            continue
        elif j >= 2:
            # increase the bet; if the player wants
            input_txt = config.Messages.CHOICE_BET_TXT
            error_msg = config.Messages.CHOICE_ERROR_TXT
            answer = get_text(player, input_txt, error_msg,
                              ['y', 'yes', 'n', 'no'])

            if answer.lower() in ['y', 'yes']:
                play[player][j][1] = bet(player, play[player][j][1])
            # if there is no increase, it will keep the previous bet
            else:
                play[player][j][1] = play[player][j][1]

            # ask the user if she wants to hit or stand
            input_txt = config.Messages.CHOICE_TYPE_TXT1
            error_msg = config.Messages.CHOICE_ERROR_TXT
            answer = get_text(player, input_txt, error_msg,
                              ['h', 'hit', 's', 'stand'])

            if answer.lower() in ['h', 'hit']:
                play[player][j][2] = 'Hit'
                continue
            else:
                play[player][j][2] = 'Stand'
                break

        # check if the hand is busted
        if play[player]['sum'] > 21:
            # check if the player likes to change the value of Aces
            print('\n########## sum > 21 #####', play[player]['sum'])
            for z in range(0, len(play[player])):
                item = play[player][z][0][0]
                if item in ['Ace', 'Ace1', 'Ace11']:
                    is_ace(player, play[player], j, item)
                    continue

            # update the bet of the new round as the previous one
            play[player][j][1] = play[player][j-1][1]
            play[player][j][2] = 'Bust'
            print(config.Messages.BUSTED_TXT.format(player,
                                                    play[player][j][1]))
            break

        j += 1

    print('\nplay_full_hand:\n',play)
    print('\n\n====================================================\n\n')


deck.deck = [['Two', 'Club'], ['Two', 'Heart'], ['Two', 'Spade'], ['Ace', 'Heart'], ['Ace', 'Diamond'], ['Ace', 'Club'], ['Ace', 'Spade'], ['Two', 'Diamond'], ['Ten', 'Heart'], ['Ten', 'Diamond'], ['Ten', 'Club'], ['Ten', 'Spade']]
print(deck.deck)

# get the first card
for i in range(0, len(players.players_name)):
    player = players.players_name[i]
    play[player] = {'sum': 0, 1: [deck.deck.pop(), 0, 'Hit']}
    is_ace(player, play[player], 1, 'Ace')
    play[player]['sum'] = sum_up(player, play[player])

# place the initial bet
for i in range(1, len(players.players_name)):
    player = players.players_name[i]
    play[player][1][1] = bet(player, 0)

print('\n\n============= First Hand ==============\n', play)

temp = players.players_name.copy()
temp.remove('Dealer')

while temp:
    print('\n================\n{}\n====================\n'.format(play))
    print(temp[0])
    play_game(temp[0], 2, 'init')
    temp.remove(temp[0])

# remove the duplicated names
for item in players.players_name:
    if item[-3:-1] == '__':
        players.players_name.remove(item[:-3])

# calculate the final results
results = {}
for item in players.players_name:
    results[item] = play[item]['sum']

print('\n\n============= Last Hand ==============\n', play)


""" sort the list based on the values and checks if any is less than 21.
    it means that there is at least a player who has not busted.
"""
names = players.players_name
if any(play[names[i]]['sum'] <= 21 for i in range(1, len(names))):
    play_game('Dealer', 2, 'play')
    results['Dealer'] = play['Dealer']['sum']

    results = sorted(results.items(), key=lambda x: x[1])

    for i in range(0, len(results)):
        if results[i][1] > 21:
            results.pop(i)

    j = 1
    for i in range(len(results)-1, -1, -1):
        print('The winner no. {} is {}'.format(j, results[-1][0]))
        if results[-1][0] != 'Dealer':
            continue
        else:
            print('Others lost the game')
            break
        j += 1
else:
    print('Dealer is the winner')
