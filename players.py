import config
from colored import fg, bg, attr
from input import get_number as get_number

# define the messages; change them in config.py
input_txt = config.Messages.PLAYER_INPUT_TXT
success_msg = config.Messages.PLAYER_SUCCESS_TXT
error_msg = config.Messages.ERROR_TXT
bet = 0

# get the number of palyers from the user
players_number = get_number('Players', 'Dealer', input_txt, success_msg,
                            error_msg, error_msg, bet)

# initiate the list of players; the first one is always the dealer
players_name = ['Dealer']

# get the name of players
for i in range(1, players_number + 1):

    player_name = str(input(config.Messages.PLAYER_NAME_TXT
                            .format(fg(31), bg(234), i, attr(0))))
    while True:
        if player_name in players_name:
            player_name = str(input(config.Messages.PLAYER_NAME_ERROR_TXT1
                                    .format(fg(1), bg(15),
                                            player_name, attr(0))))
        elif player_name[-3:-1] == '__':
            player_name = str(input(config.Messages.PLAYER_NAME_ERROR_TXT2
                                    .format(fg(1), bg(15), attr(0))))
        else:
            break
    players_name.append(player_name)
