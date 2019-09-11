from collections import namedtuple
from IPython.display import clear_output

def replay():
    replay = input('Do you want to play again ?\t')
    while replay not in ['Yes','No']:
        replay = input('Yes or No, Do you want to play again ?\t')
    return replay == 'Yes'

def symbol(mark, anti):
    if mark == 'X':
        if anti == 0:
            return 'X'
        return 'O'
    if anti == 0:
        return 'O'
    return 'X'

def mark_players():
    Player = namedtuple('player', 'num, mark')
    turn = input('Player 1 do you want play first ?\t')
    while turn not in ['Yes','No']:
        turn = input('Yes or No, Do you want play first ?\t')
    mark = input('Player 1 X or O ?\t')
    while mark not in ['X','O']:
        mark = input('Please X or O ?\t')
    player = list()
    if turn == 'Yes':
        player.append(Player(1, symbol(mark, 0)))
        player.append(Player(2, symbol(mark, 1)))
    else:
        player.append(Player(2, symbol(mark, 1)))
        player.append(Player(1, symbol(mark, 0)))
    return player

def finish_check(board, mark):
    if board[:3] == [mark] * 3:
        return 1
    if board[3:6] == [mark] * 3:
        return 1
    if board[6:] == [mark] * 3:
        return 1
    if board[0] == board[3] == board[6] == mark:
        return 1
    if board[1] == board[4] == board[7] == mark:
        return 1
    if board[2] == board[5] == board[8] == mark:
        return 1
    if board[4] == mark:
        if board[0] == board[8] == mark:
            return 1
        if board[2] == board[6] == mark:
            return 1
    return 0

def finish(board):
    if finish_check(board, 'X'):
        return 1
    if finish_check(board, 'O'):
        return 2
    if ' ' in board:
        return 0
    return 3

def print_result(board, result):
    draw_board(board)
    if result < 3:
        print(f'Player {result} WIN\n')
    else:
        print('Draw Match\n')

def draw_board(board):
    clear_output()
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[6],board[7],board[8]))
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[3],board[4],board[5]))
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[0],board[1],board[2]))
    print("   |   |   ")

def fill_turn(board, player_num):
    ''' n mean turn '''
    move = input("Player {} your move:  ".format(player_num))
    while 1:
        if move not in "123456789":
            move = input("choose a number between 1 and 9:  ")
        elif board[int(move)-1] != ' ':
            move = input("This place is already token, choose another one:  ")
        else:
            break
    return int(move)

def print_instructs():
    print("It's a simple Tic Tac Toe game")
    print("Use the numpad for choosing the move")
    print("   7 | 8 | 9 ")
    print("  -----------")
    print("   4 | 5 | 6 ")
    print("  -----------")
    print("   1 | 2 | 3 ")
    print('\n'*3)

while 1:
    print_instructs()
    player = mark_players()
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    result = finish(board)
    i = 0
    while result == 0:
        draw_board(board)
        board[fill_turn(board, player[i%2].num) - 1] = player[i%2].mark
        result = finish(board)
        print('\n'*3)
        i += 1
    print_result(board, result)
    if not replay():
        break
