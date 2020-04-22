from IPython.display import clear_output

def display_board(board):
    clear_output()
    print('-----')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-----')
def player_input():
    marker=''
    while marker!='X' and marker!='O':
        marker=input('Player 1, choose X or O: ')
    player1=marker
    if player1=='X':
        player2='O'
    else:
        player2='X'
    return (player1,player2)
def place_marker(board, marker, position):
    board[position]=marker
    display_board(board)
def win_check(board, marker):
    if (board[7] == board[8] == board[9] == marker) or (board[4] == board[5] == board[6] == marker) or (board[1] == board[2] == board[3] == marker) or (board[7] == board[5] == board[3] == marker) or (board[1] == board[5] == board[9] == marker) or (board[1] == board[4] == board[7] == marker) or (board[2] == board[5] == board[8] == marker) or (board[3] == board[6] == board[9] == marker):
        display_board(board)
        print('Congratulations!'+' Player'+str(dic[marker])+' '+marker+' Has Won')
        return True
    else:
        return False
import random

def choose_first():
    if random.randint(1,2)==1:
        marker=player1_marker
        return 'Player1'
    else:
        marker=player2_marker
        return 'Player2'
def space_check(board, position):
    if board[position]!='X' and board[position]!='O':
        return True
    else:
        return False
def full_board_check(board):
    for e in board:
        if e!='X' and e!='O':
            return False
    else:
        return True
def player_choice(board):
    while True:
        choice=0
        while choice not in range(1,10):
            display_board(board)
            choice=int(input('Player'+str(dic[marker])+' '+marker+' Enter position: '))
        if space_check(board,choice):
            return choice
        else:
            continue
def replay():
    play=input('Do you want to play again (y/n): ')
    if play=='y':
        return True
    else:
        return False
while True:
    clear_output()
    print('Welcome to Tic Tac Toe!')
    board = ['X',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1_marker,player2_marker=player_input()
    dic={player1_marker:1,player2_marker:2}
    if choose_first()=='Player1':
        marker=player1_marker
        print('Player1 Goes First')
    else:
        marker=player2_marker
        print('Player2 Goes First')
    while True:
        position=player_choice(board)
        place_marker(board, marker, position)
        if win_check(board, marker):
            break
        if marker==player1_marker:
             marker=player2_marker
        else:
             marker=player1_marker
        if (full_board_check(board)==True) and (win_check(board, marker)==False):
            print('Its Tie')
            break
    if not replay():
        break
