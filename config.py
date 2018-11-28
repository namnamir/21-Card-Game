class Default:
    ACE_VALUE = None
    JACK_VALUE = 1
    QUEEN_VALUE = 2
    KING_VALUE = 3


class Messages:
    ERROR_TXT = '"{}" is not a natural number.\nPlease enter a '\
                'valid natural number like 1 or 23!'

    PLAYER_INPUT_TXT = '{}! How many players are going to play? '
    PLAYER_SUCCESS_TXT = '{} players are going to play 21.'
 
    ACE_INPUT_TXT = '{}! What is the value of Ace; 1 or 11? '
    ACE_SUCCESS_TXT = 'Ace will be assumed as {}. '\
                    'You can change it later.'
    ACE_ERROR_TXT = 'Ace can be either 1 or 11. '\
                    '{} is none of them.\nPlease enter 1 or 11.'

    BET_INPUT_TXT = '{}! How much do you want to bet? '
    BET_SUCCESS_TXT = 'Your bet is increased to {}.'
    BET_ERROR_TXT1 = 'Your new bet should be higher than the previous'\
                     ' one.\nPlease enter a bet higher than {}.'

    CHOICE_TYPE_TXT1 = '{}! Do you like to hit or stand? (H/S) '
    CHOICE_TYPE_TXT2 = '{}! Do you like to split your hand? (Y/N) '
    CHOICE_BET_TXT = '{}! Do you like to increase your bet? (Y/N) '
    CHOICE_ERROR_TXT = 'You need to choose among the options: {}; '\
                       'it is not case-sensitive.'
   
    BUSTED_TXT = '{}! Oops, you brusted and unfortunately lost {}.'
    WON_TXT = '{}! Congrats, you won {}.'