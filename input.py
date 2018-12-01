def get_number(Flag, player_name, input_text, success_text, error_text1,
               error_text2, previous_bet):
    while True:
        try:
            # get the input from the user
            number = str(input(input_text.format(str(player_name))))
            # checks if it is an int
            number = int(number)
            # if it gets the Ace value from the user
            if Flag == 'Ace':
                # checks if it is either 1 or 11; it can't get any other value
                if number == 1 or number == 11:
                    print(success_text.format(str(number)))
                    # correct the value of Ace
                    if number == 11:
                        return 'Ace11'
                    else:
                        return 'Ace1'
                    break
                # if the value of Ace is an int but not 1 or 11
                else:
                    print(error_text1.format(str(number)))
                    continue
            elif Flag == 'Bet':
                # checks if the bet is bigger than the previous one
                if number >= previous_bet:
                    print(success_text.format(str(number)))
                    return number
                    break
                # if the new bet is smaller than the previous one
                else:
                    print(error_text1.format(str(previous_bet)))
                    continue
            # if it is none of the above
            print(success_text.format(str(number)))
            return number
            break
        # if it is not an int, shows an error message and try agian
        except ValueError:
                print(error_text2.format(str(number)))
                continue


def get_text(player_name, input_text, error_text, array):
    while True:
        try:
            # get the input from the user
            text = str(input(input_text.format(str(player_name))))
            # if it gets the Ace value from the user
            if text.lower() in array:
                return text
                break
            # if the value of Ace is an int but not 1 or 11
            else:
                print(error_text.format(str(array)))
                continue
        # if it is not an int, shows an error message and try agian
        except ValueError:
                print(error_text.format(str(array)))
                continue
