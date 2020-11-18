'''tic tac toe solution as complete .py file 
'''
import os
import random
from time import sleep

LINE = 11 * "-"
EMPTY = " "

def make_row():
    # row = []
    # for column in range(0,3):
    #     row.append(EMPTY)
    # return row
    return [EMPTY, EMPTY, EMPTY]

def make_board():
    game_board = []
    for row in range(0, 3):
        row = make_row()
        game_board.append(row)    
    return game_board 

def display_space(board, row, space):
    print(f" {board[row][space]} ", end="")

def display_row(board, row):
    for space in range(0,3):
        display_space(board, row, space)
        if space < 2:
            print("|", end="")
        else:
            print()

def display_board(board):
    os.system('cls||clear')

    for r in range (0,3):
        display_row(board, r)
        if r < 2:
            print(LINE)


def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')   

def place_marker(board, row, column, marker):
    board[row][column] = marker


def check_row_win(board):
    win_r0 = board[0][0] != EMPTY and board[0][0] == board[0][1] == board[0][2]
    win_r1 = board[1][0] != EMPTY and board[1][0] == board[1][1] == board[1][2]
    win_r2 = board[2][0] != EMPTY and board[2][0] == board[2][1] == board[2][2]
    return win_r0 or win_r1 or win_r2

def check_column_win(board):
    win_c0 = board[0][0] != EMPTY and board[0][0] == board[1][0] == board[2][0]
    win_c1 = board[0][1] != EMPTY and board[0][1] == board[1][1] == board[2][1]
    win_c2 = board[0][2] != EMPTY and board[0][2] == board[1][2] == board[2][2]
    return win_c0 or win_c1 or win_c2

def check_diagonal_win(board):
    # check for diagonal win
    win_d1 = board[0][0] != EMPTY and board[0][0] == board[1][1] == board[2][2]
    win_d2 = board[2][0] != EMPTY and board[2][0] == board[1][1] == board[0][2]
    return win_d1 or win_d2

def check_win(board):
    return check_row_win(board) or check_column_win(board) or check_diagonal_win(board)

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, row, column):
    return board[row][column] == EMPTY

def check_full(board):
    full = True
    for row in range(0, 3):
        for space in range(0,3):
            if board[row][space] == EMPTY:
                full = False
                break
    return full

def player_choice(board):
    valid_choice = False
    while not valid_choice:
        user_entry = input("Please enter your next move as row, column (x,y) ")
        try:
            x, y = user_entry.split(",")
            row = int(x)
            column = int(y)
            if space_check(board, row, column):
                valid_choice = True
            else:
                print("That space is taken!")
        except :
            print("Sorry, that is not a valid move. Please try again.")

    return row, column

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

### game starts here ###
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = make_board()
    display_board(theBoard)
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(f"{turn} will go first.")
    
    play_game = input("Are you ready to play? Enter Yes or No. ")
    
    if play_game.lower()[0] == 'n':
        break

    display_board(theBoard)
    game_on = True
    while game_on:
        
        row, column = player_choice(theBoard)
        if turn == "Player 1":
            marker = player1_marker
            next_turn = "Player 2"
        else:
            marker = player2_marker
            next_turn = "Player 1"
        place_marker(theBoard, row, column, marker)
        display_board(theBoard)
        if check_win(theBoard):
            print(f'{turn} has won!')
            game_on = False
        elif check_full(theBoard):
            print('The game is a draw!')
            game_on = False
        else:
            turn = next_turn

    if not replay():
        break

print("Okay. Bye!")
