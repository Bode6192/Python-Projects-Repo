theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def check_win(turn):
    if (theBoard['7'] == theBoard['8'] == theBoard['9'] == turn) or (theBoard['6'] == theBoard['5'] == theBoard['4'] == turn):
        return True
    elif (theBoard['1'] == theBoard['2'] == theBoard['3'] == turn) or (theBoard['7'] == theBoard['5'] == theBoard['3'] == turn):
        return True
    elif theBoard['1'] == theBoard['5'] == theBoard['9'] == turn or theBoard['1'] == theBoard['4'] == theBoard['7'] == turn:
        return True
    elif theBoard['2'] == theBoard['5'] == theBoard['8'] == turn or theBoard['3'] == theBoard['6'] == theBoard['9'] == turn:
        return True


turn = 'X'
for i in range(9):
    printBoard(theBoard)
    move = input('Turn for ' + turn + '. Move on which space?')
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    if check_win(turn):
        print(turn + '  you win. Congratulations!!!')
        break
printBoard(theBoard)
