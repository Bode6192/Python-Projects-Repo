def main():

    game_list = [0, 1, 2]

    def display_game(game_list):
        print('Here is the current list: ')
        print(game_list)

    
    def position_choice():
        choice = 'wrong'

        while choice not in ['0', '1', '2']:
            choice = input('Please enter a valid position choice, either (0, 1, 2): ')

            if choice not in ['0', '1', '2']:
                print('Sorry, invalid choice! ')
        
        return int(choice)
    

    def replacement_choice(game_list, position):
        user_placement = input('Type a string to place at position: ')

        game_list[position] = user_placement

        return game_list


    def game_on_choice():
        choice = 'wrong'

        while choice not in ['Y', 'N']:
            choice = input('Do you want to kep playing? (Y or N): ').upper()

            if choice not in ['Y', 'N']:
                print('Sorry, invalid choice! Please choose Y or N ')
        
        if choice == 'Y':
            return True
        else:
            return False


    game_on = True
    game_list = [0, 1, 2]

    while game_on:
        display_game(game_list)

        position = position_choice()

        game_list = replacement_choice(game_list, position)

        display_game(game_list)

        game_on = game_on_choice()


if __name__ == '__main__':
    main()

