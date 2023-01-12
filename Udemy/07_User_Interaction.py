from turtle import position

game_list = [0,1,2]

def display_game(game_list):
    print('Here is the game list: ')
    print(game_list)

print(display_game(game_list))

def position_choice():

    choice = 'wrong'

    while choice not in ['0', '1', '2']:

        choice = input('Pick a position (0,1,2): ')

        if choice not in ['0', '1', '2']:
            print('Sorry, invalid choice')

    return int(choice)


def replacement_choice(game_list, position):
    user_placement = input('Type a string to place at the game list position: ')

    game_list[position] = user_placement

    return game_list

def gameon_choice():

    choice = 'wrong'

    while choice not in ['Y', 'N']:

        choice = input("Keep playing? 'Y' or 'N: ").upper()

        if choice.upper() not in ['Y','N']:
            print('Sorry, i dont understand, please choose y or n')


    if choice == "Y":
        return True
    else :
        return False


game_on = True
game_list = [0,1,2]

while game_on:

    display_game(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list, position)

    display_game(game_list)

    game_on = gameon_choice()

