import random


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
    player_1 = ''
    player_2 = ''
    first_player = choose_first()
    print(first_player + ' selects his marker first')
    print('Whoever selects X goes first')

    marker = input("Do you want to be 'X' or 'O'? ").upper()
    while marker not in ['X', 'O']:
        print()
        print('Invalid Input!!!')
        marker = input("Do you want to be 'X' or 'O'? ").upper()
    if first_player == 'Player 1':
        player_1 = marker
    else:
        player_2 = marker

    if player_1 == 'X':
        player_2 = 'O'
    elif player_1 == 'O':
        player_2 = 'X'
    elif player_2 == 'O':
        player_1 = 'X'
    else:
        player_1 = 'O'
        player_2 = 'X'
        

    return (player_1, player_2)


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
    if board[position] == ' ':
        return True
    return False


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    while True:
        position = input('Enter your desired position from (1-9): ')
        if position not in list(str(i) for i in range(1,10)):
            print('Sorry, your entry is not in the range (1-9), 9 inclusive')
        if space_check(board, int(position)) == False:
            print('Sorry, this space has already been used')
        else:
            break
        print()

    return int(position)


def replay():
    
    while True:
        replay = input('Do you both want to replay? (Y or N): ').upper()
        if replay not in ['Y', 'N']:
            print('Sorry, not a valid input')
        else:
            break
        print()
    
    return replay == 'Y'



# GAME
while True:
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    display_board(board)

    game_on = True

    player_1_marker, player_2_marker = player_input()

    if player_1_marker == 'X':
        turn = 'Player 1'
    else:
        turn = 'Player 2'

    while game_on:
        if turn == 'Player 1':
            marker = player_1_marker
            print("Player 1 it's your turn")
        else:
            marker = player_2_marker
            print("Player 2 it's your turn")
        
        position = player_choice(board)
        place_marker(board, marker, position)
        display_board(board)
        if win_check(board, marker):
            print('Congratulations ' + turn + ' you win!!!')
            break
        elif full_board_check(board):
            print('GAME OVER!!!')
            break

        if turn == 'Player 1':
            turn = 'Player 2'
        else:
            turn = 'Player 1'
        

    if replay():
        continue
    else:
        break

        

