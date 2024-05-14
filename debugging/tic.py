#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if all(cell == row[0] and cell != " " for cell in row):
            return True

    for col in range(len(board[0])):
        if all(board[row][col] == board[row+1][col] == board[row+2][col] and board[row][col] != " " for row in range(len(board)-2)):
            return True

    if all(board[i][i] == board[i+1][i+1] == board[i+2][i+2] and board[i][i] != " " for i in range(len(board)-2)):
        return True

    if all(board[i][2-i] == board[i+1][1-i] == board[i+2][0-i] and board[i][2-i] != " " for i in range(len(board)-2)):
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    turn = 0
    while turn < 9:
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if board[row][col] == " ":
                board[row][col] = player
                turn += 1
                if check_winner(board):
                    print_board(board)
                    print("Player " + player + " wins!")
                    return
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError:
            print("Please enter a valid integer.")
        except IndexError:
            print("Please enter a value between 0 and 2.")

    print_board(board)
    print("It's a draw!")

tic_tac_toe()
