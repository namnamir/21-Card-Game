import deck
import players
from input import get_text as get_text
from input import get_number as get_number
import config
from colored import fg, bg, attr
from terminaltables import SingleTable


play = {}

status = ['Stand', 'Hit', 'Bust', 'Split']


# print the hand
def print_hand(player, Flag):
    for i in range(1, sorted(play[player].keys())[-1] + 1):
        deck.print_card(play[player][i][0], 'Print')
    if Flag == 'Print_Sum':
        deck.print_sum(play[player][0])


# update the bet
def bet(player_name, previous_bet):
    # define the messages; change them in config.py
    input_txt = config.Messages.BET_INPUT_TXT
    success_msg = config.Messages.BET_SUCCESS_TXT
    error_msg1 = config.Messages.BET_ERROR_TXT1
    error_msg2 = config.Messages.ERROR_TXT
    # set the new bet
    return get_number('Bet', player_name, input_txt, success_msg, error_msg1,
                      error_msg2, previous_bet)


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
        player[0] = sum_up(player_name, player)

    # # print the hand after defining the value of the Ace
    # print(config.Messages.CARD_DETAILS_TXT4.format(fg(3), bg(234), player,
    #                                                attr(0)))
    # for i in range(1, sorted(player.keys())[-1] + 1):
    #     deck.print_card(player[i][0])
    # deck.print_sum(player[0])
    # print(player)


# sum up the value of cards
def sum_up(player_name, player):
    sum_value = 0
    for key in list(player.keys()):
        if key == 0:
            continue
        sum_value += deck.ranks[player[key][0][0]]
    return sum_value


# define the winner and print the final table
def print_statistics(player, Flag):
    table = [['Player Name', 'Cards', 'Sum', 'Bet', 'Status']]
    temp2 = {}  # for collecting sums
    temp3 = []  # for collecting equal sums
    equal_val = 0

    for name in player:
        temp1 = []  # for forming rows of the table
        last_card = sorted(play[name].keys())[-1]
        a = ''

        # set a dic {name:sum} to find the winner
        temp2[name] = play[name][0]

        temp1.append(name)  # name
        for x in range(1, last_card + 1):
            a += deck.print_card(play[name][x][0], None)
            if x < last_card:
                a += ' - '
        temp1.append(a)  # hand
        temp1.append(play[name][0])  # sum
        temp1.append(play[name][last_card][1])  # bet
        if temp1[2] > 21:  # status
            temp1.append('Busted')  # status
        elif temp1[2] == 21:
            temp1.append('Won')  # status
        else:
            temp1.append('Lost')  # status
        table.append(temp1)

    # set the statuses in case all are busted before the Dealer start playing
    if Flag == 'All_Busted':
        table[1][1] = '-'
        table[1][2] = '-'
        table[1][4] = 'Won'
        print(config.Messages.ALL_BUSTED_TXT.format(fg(3), bg(234), attr(0)))

    else:
        # sort descendingly the results and remove the busted players
        temp2 = list(reversed(sorted(temp2.items(), key=lambda x: x[1])))
        for i in range(0, len(temp2)):
            if temp2[i][1] > 21:
                temp2.pop(i)
                continue
            # if 2 or more players have the same sum
            try:
                # to be sure that the last item is taken into account
                if i == len(temp2) - 1 and temp2[i][1] == equal_val:
                    temp3.append(temp2[i][0])
                # if first items (>= 2) are eqals
                elif i < len(temp2) and temp2[i][1] == temp2[i+1][1]:
                    temp3.append(temp2[i][0])
                    equal_val = temp2[i][1]
            except IndexError:
                pass

        # if the Dealer and others have the highest score the Dealer wins
        if temp2[0][0] and 'Dealer' in temp3:
            for item in table:
                if item[0] in temp3:
                    if item[0] != 'Dealer':
                        item[4] = 'Lost'
                    else:
                        item[4] = 'Won'
            print(config.Messages.WON_TXT2.format(attr(5), fg(15), bg(160),
                                                  'Dealer', attr(0)))
        # if more than one wins, change the status of all to 'Won'
        elif temp2[0][0] in temp3 and len(temp3) > 1:
            for name in temp3:
                for row in table:
                    if row[0] == name:
                        row[4] = 'Won'
                        print(config.Messages.WON_TXT3.format(attr(5), fg(15),
                                                              bg(160), name,
                                                              attr(0)))
                        break
        # if none of the above, the winner is the first member of temp2
        else:
            for row in table:
                if row[0] == temp2[0][0]:
                    row[4] = 'Won'
                    break
            print(config.Messages.WON_TXT2.format(attr(5), fg(15), bg(160),
                                                  temp2[0][0], attr(0)))

    # print the statisctics
    table = SingleTable(table)
    print(table.table)


# get the second, third and more card for each player
def play_game(player, j, Flag):
    play[player][0] = sum_up(player, play[player])
    while play[player][0] <= 21 and play[player][j-1][2] == 'Hit':

        # initiate the round
        play[player][j] = [None, 0, None]

        # get a new card
        play[player][j][0] = deck.deck.pop()

        # print the new card and check if it is the ace or not
        print(config.Messages.CARD_DETAILS_TXT2.format(fg(3), bg(234),
                                                       player, j, attr(0)))
        deck.print_card(play[player][j][0], 'Print')
        is_ace(player, play[player], j, 'Ace')

        """ check if split is eligible
            if it is exactly the scond hand && the last to chars before the
            last one of the name of the palyer is not __ && the palayer is the
            Dealer && two first cards have the same value
        """
        if j == 2 and player[-3:-1] != '__' and player != 'Dealer' and \
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
                play[player + '__1'][0] = int(play[player][0] / 2)
                play[player + '__2'][0] = int(play[player][0] / 2)

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

        """if it's Dealer's turn, there are some rules:
           The Dealer must hit when it has a total of 16 points or less
           and must stand with a total of 17 points or more.
        """
        play['Dealer'][0] = sum_up('Dealer', play['Dealer'])
        if player == 'Dealer' and play['Dealer'][0] <= 16:
            play[player][j][2] = 'Hit'
            j += 1
            continue
        elif player == 'Dealer' and play['Dealer'][0] >= 17:
            if play['Dealer'][0] == 21:
                play[player][j][2] = 'Won'
            elif play['Dealer'][0] > 21:
                play[player][j][2] = 'Busted'
            else:
                play[player][j][2] = 'Stand'
            break

        # check if the hand is 21
        play[player][0] = sum_up(player, play[player])
        if play[player][0] == 21:
            # update the bet of the new round as the previous one
            play[player][j][1] = play[player][j-1][1]
            print(config.Messages.WON_TXT1.format(attr(5), fg(15), bg(160),
                                                  player,
                                                  play[player][j-1][1],
                                                  attr(0)))
            break

        # if the player is not the Dealer
        if j >= 2 and play[player][0] < 21:
            # ask the player if she wants to increase the bet
            input_txt = config.Messages.CHOICE_BET_TXT
            error_msg = config.Messages.CHOICE_ERROR_TXT
            answer = get_text(player, input_txt, error_msg,
                              ['y', 'yes', 'n', 'no'])
            if answer.lower() in ['y', 'yes']:
                play[player][j][1] = bet(player, play[player][j-1][1])
                bet_flag = 'Increased'  # the bet is increased

            # ask the player if she wants to hit or stand
            input_txt = config.Messages.CHOICE_TYPE_TXT1
            error_msg = config.Messages.CHOICE_ERROR_TXT
            answer = get_text(player, input_txt, error_msg,
                              ['h', 'hit', 's', 'stand'])
            if answer.lower() in ['h', 'hit']:
                play[player][j][2] = 'Hit'
                j += 1
                continue
            else:
                play[player][j][2] = 'Stand'
                break
            """update the bet of the new round as the previous one if
               it is not already increased by the player
            """
            if bet_flag != 'Increased':
                play[player][j][1] = play[player][j-1][1]

        # check if the hand is busted
        elif play[player][0] > 21:

            # check if the player likes to change the value of Aces
            for z in range(1, len(play[player])):
                item = play[player][z][0][0]
                if item in ['Ace', 'Ace1', 'Ace11']:
                    print(config.Messages.BUSTED_C_TXT.format(attr(5), fg(15),
                                                              bg(160), player,
                                                              play[player][j-1][1],
                                                              attr(0)))

                    print_hand(player, 'Print_Sum')

                    break
                    is_ace(player, play[player], z, item)
                    play[player][0] = sum_up(player, play[player])
                    continue

            # update the bet of the new round as the previous one
            play[player][j][1] = play[player][j-1][1]
            play[player][j][2] = 'Bust'
            # print the message as the busted hand
            print(config.Messages.BUSTED_TXT.format(attr(1), attr(5), fg(1),
                                                    bg(15), player,
                                                    play[player][j][1]))
            print_hand(player, 'Print_Sum')
            break

        # print the value of each card + the sum of them
        print(config.Messages.CARD_DETAILS_TXT3.format(fg(3), bg(234),
                                                       player, j, attr(0)))
        for i in range(1, sorted(play[player].keys())[-1] + 1):
            deck.print_card(play[player][i][0], 'Print')
        deck.print_sum(play[player][0])

        j += 1

    print('\n<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>')
    print(config.Messages.CARD_DETAILS_TXT5.format(fg(3), bg(234),
                                                   player, attr(0)))
    print_hand(player, 'Print_Sum')
    print('<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>\n')


player = players.players_name

# get the first card
for name in player:
    play[name] = {0: 0, 1: [deck.deck.pop(), 0, 'Hit']}
    is_ace(player, play[name], 1, 'Ace')
    play[name][0] = sum_up(name, play[name])

# place the initial bet; except for the Dealer
print(config.Messages.CARD_DETAILS_TXT1.format(fg(3), bg(234), name, attr(0)))

# print the initial hand of each player and ask for the first bet
for i in range(1, len(player)):
    print_hand(player[i], None)
    play[player[i]][1][1] = bet(player[i], 0)

# create a temporary array which helps with splited hands
temp1 = player.copy()
temp1.remove('Dealer')

while temp1:
    play_game(temp1[0], 2, 'init')
    temp1.remove(temp1[0])

# remove the duplicated names
for item in player:
    if item[-3:-1] == '__':
        player.remove(item[:-3])

# calculate the final results
# results = {}
# for item in player:
#     results[item] = play[item][0]


""" sort the list based on the values and checks if any is less than 21.
    it means that there is at least a player who has not busted.
"""
if any(play[player[i]][0] <= 21 for i in range(1, len(player))):
    play_game('Dealer', 2, 'play')
    print_statistics(player, 'Check')

else:
    print_statistics(player, 'All_Busted')
