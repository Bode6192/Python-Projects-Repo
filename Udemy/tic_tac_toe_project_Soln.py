import random
from turtle import position


def display_board(board):
    print('\n' * 10)
    print(' | | ')
    print(f'{board[7]}|{board[8]}|{board[9]}')
    print(' | | ')
    print('-----')
    print(' | | ')
    print(f'{board[4]}|{board[5]}|{board[6]}')
    print(' | | ')
    print('-----')
    print(' | | ')
    print(f'{board[1]}|{board[2]}|{board[3]}')
    print(' | | ')


def player_input():

    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''

    marker = ''
    while marker != 'X' and marker != 'O':
       marker = input("Player 1: Do you want to be 'X' or 'O'? ").upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return('O', 'X')


def place_marker(board, marker, position):

    board[position] = marker


def win_check(board, mark):
    if (board[7] == board[8] == board[9] == mark) or (board[6] == board[5] == board[4] == mark):
        return True
    elif (board[1] == board[2] == board[3] == mark) or (board[7] == board[5] == board[3] == mark):
        return True
    elif board[1] == board[5] == board[9] == mark or board[1] == board[4] == board[7] == mark:
        return True
    elif board[2] == board[5] == board[8] == 'X' or board[3] == board[6] == board[9] == mark:
        return True


def choose_first():
    first_player = random.randint(1, 2)

    if first_player == 1:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9) '))

    return position


def replay():
    
    while True:
        replay = input('Do you both want to replay? (Y or N): ').upper()
        if replay not in ['Y', 'N']:
            print('Sorry, not a valid input')
        else:
            break
        print()
    
    return replay == 'Y'


# WHILE LOOP TO KEEP RUNNING THE GAME
print('Welcome to Tic Tac Toe')

while True:
    # PLAY THE GAME
    
    # SET EVERYTHING UP(BOARD, WHO'S FIRST, CHOOSE MARKERS X,O)
    theboard = [' ']*10
    player_1_marker, player_2_marker = player_input()

    turn = choose_first()
    print(turn +' will go first')

    play_game = input('Ready to play? Y or N: ').upper()


    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    
    # GAME PLAY

    while game_on:

        if turn == 'Player 1':

            display_board(theboard)

            position = player_choice(theboard)

            place_marker(theboard, player_1_marker, position)

            if win_check(theboard, player_1_marker):
                display_board(theboard)
                print('PLAYER 1 HAS WON!!!')
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('TIE GAME!!!')
                    break
                else:
                    turn = 'Player 2'
            
            ### PLAYER ONE TURN

        else:
            display_board(theboard)

            position = player_choice(theboard)

            place_marker(theboard, player_2_marker, position)

            if win_check(theboard, player_2_marker):
                display_board(theboard)
                print('PLAYER 2 HAS WON!!!')
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('TIE GAME!!!')
                    break
                else:
                    turn = 'Player 1'

    
    if not replay():
        break