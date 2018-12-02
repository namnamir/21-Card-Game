class Default:
    ACE_VALUE = 11
    JACK_VALUE = 1
    QUEEN_VALUE = 2
    KING_VALUE = 3


class Messages:
    ERROR_TXT = ' {}{} "{}" is not a natural number. Please ' \
                'enter a valid natural number like 1 or 23! {}'

    PLAYER_INPUT_TXT = ' {}{} {}! How many players are going to play? {} '
    PLAYER_SUCCESS_TXT = ' {}{} {} players are going to play 21. {}\n'

    PLAYER_NAME_TXT = ' {}{} Dealer! Please enter the name of player no. {}' \
                      ': {} '
    PLAYER_NAME_ERROR_TXT1 = ' {}{} "{}" is a duplicated name; try again!: {} '
    PLAYER_NAME_ERROR_TXT2 = ' {}{} "__" at the end of the name is not ' \
                             'acceptable; try again!: {} '

    ACE_INPUT_TXT = '\n {}{} {}! What is the value of Ace; 1 or 11? {}'
    ACE_SUCCESS_TXT = ' {}{} The value of Ace will be assumed as {}. ' \
                      'You can change it later.{}\n'
    ACE_ERROR_TXT = ' {}{} Ace can be either 1 or 11. ' \
                    '{} is none of them. Please enter 1 or 11.{}'

    BET_INPUT_TXT = '\n {}{} {}! How much do you want to bet?{} '
    BET_SUCCESS_TXT = ' {}{} Your bet is increased to {}. {}\n'
    BET_ERROR_TXT1 = ' {}{} Your new bet should be higher than zero while ' \
                     '{} is smaller or equals to zero. {}'
    BET_ERROR_TXT2 = ' {}{} Your new bet should be higher than the previous ' \
                     'one. Please enter a bet higher than {}. {}'

    CHOICE_TYPE_TXT1 = '\n {}{} {}! Do you like to hit or stand? (H/S) {} '
    CHOICE_TYPE_TXT2 = '\n {}{} {}! Do you like to split your hand? (Y/N) {} '
    CHOICE_BET_TXT = '\n {}{} {}! Do you like to increase your bet? (Y/N) {} '
    CHOICE_ERROR_TXT = ' {}{} You need to choose among the options: {}; ' \
                       'it is not case-sensitive. {}'

    BUSTED_TXT = ' {}{}{} Oops!!! {}, you brusted and unfortunately lost {}. '\
                 'Your had was: {}'
    BUSTED_C_TXT = ' {}{}{} {}!, you brusted but fortunately you have ACe(s) '\
                   'in your had; you can change their values: {}'
    ALL_BUSTED_TXT = ' {}{} Oops!!! All are busted then the winner is the ' \
                     'Dealer. The statistics of the game is: {}'

    WON_TXT1 = ' {}{}{} {}! Congrats, you probably won {} (equals your bet) ' \
               'in the second hand. But the game continues. {} '
    WON_TXT2 = ' {}{}{} {} is the winner. {} '
    WON_TXT3 = ' {}{}{} One of the winners is {}. {} '

    CARD_DETAILS_TXT1 = '\n {}{} {}! Your initial hand consists of: {}'
    CARD_DETAILS_TXT2 = ' {}{} {}! The new card in the round {} is: {}'
    CARD_DETAILS_TXT3 = '\n {}{} {}! Your hand, in the round {}, ' \
                        'consist of: {}'
    CARD_DETAILS_TXT4 = '\n {}{} {}! Your hand, after defining the value of ' \
                        'Ace, consists of: {}'
    CARD_DETAILS_TXT5 = '\n {}{} {}! Your completed hand consists of: {}'
