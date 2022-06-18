import random


def display_board(board):
    print(' '+board[6]+' | '+board[7]+' | '+board[8])
    print('-----------')
    print(' '+board[3]+' | '+board[4]+' | '+board[5])
    print('-----------')
    print(' '+board[0]+' | '+board[1]+' | '+board[2])


board = [' ' for x in range(9)]


def choose_first():
    return random.randint(1, 2)


def input_position(q):
    p = int(input("Enter the position you want to place in:\n"))
    if(check_space(p)):
        board[p-1] = q
        display_board(board)
    else:
        f = full_board_check(board)
        if(f == True):
            print("This position is already taken.\n")
            return input_position(q)
        else:
            print("It's a draw!!")


def full_board_check(board):
    if ' ' in board:
        return True
    else:
        return False


def win_check():
    if ((board[0] == board[3] == board[6]) and board[0] != ' ' and board[3] != ' ' and board[6] != ' ') or ((board[1] == board[4] == board[7]) and board[1] != ' ' and board[4] != ' ' and board[7] != ' ') or ((board[2] == board[5] == board[8]) and board[2] != ' ' and board[5] != ' ' and board[8] != ' ') or ((board[0] == board[1] == board[2]) and board[0] != ' ' and board[1] != ' ' and board[2] != ' ') or ((board[3] == board[4] == board[5]) and board[3] != ' ' and board[4] != ' ' and board[5] != ' ') or ((board[6] == board[7] == board[8]) and board[6] != ' ' and board[7] != ' ' and board[8] != ' ') or ((board[0] == board[4] == board[8]) and board[4] != ' ' and board[0] != ' ' and board[8] != ' ') or ((board[2] == board[4] == board[6]) and board[2] != ' ' and board[4] != ' ' and board[6] != ' '):
        return True
    else:
        return False


def check_space(p):
    if(board[p-1] == ' '):
        return True
    else:
        return False


def replay():
    j = input("Do you want to play again?\n")
    if(j.lower() == "yes"):
        board = [' ' for x in range(9)]
        play_game()
    else:
        print("Thank you for playing")


def play_game():
    global board
    board = [' ' for x in range(9)]
    print("\nWelcome to TICTACTOE\n")
    print("This is the outline of the board. Please use this as a reference for entering the correct position.\n")
    print(' 7 | 8 | 9 ')
    print('-----------')
    print(' 4 | 5 | 6 ')
    print('-----------')
    print(' 1 | 2 | 3 \n')
    x = choose_first()
    print(f"Player {x} goes first\n")
    f = True
    w = True
    while(f == True):
        input_position('X')
        w = win_check()
        if(w == True):
            if(x == 1):
                print("PLAYER 1 WON!")
            else:
                print("PLAYER 2 WON!")
            replay()
            break
        else:
            f = full_board_check(board)
            if(f == False):
                print("It's a draw!!")
                replay()
        input_position('O')
        w = win_check()
        if(w == True):
            if(x == 1):
                print("PLAYER 2 WON!")
            else:
                print("PLAYER 1 WON!")
            replay()
            break
        else:
            f = full_board_check(board)
            if(f == False):
                print("It's a draw!!")
                replay()
                break


play_game()
