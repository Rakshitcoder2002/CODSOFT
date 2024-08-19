# -*- coding: utf-8 -*-
"""TIC TAC TOE AI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iN3tHOVcCq6XDB760oXZKrYcQiAFsYzr
"""

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    ...

def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def get_valid_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner:
        return {'X': 1, 'O': -1, 'Draw': 0}[winner]

    if is_draw(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for move in get_valid_moves(board):
            board[move[0]][move[1]] = 'X'
            eval = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_valid_moves(board):
            board[move[0]][move[1]] = 'O'
            eval = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board, player):
    best_val = float('-inf') if player == 'X' else float('inf')
    best_move = None

    for move in get_valid_moves(board):
        board[move[0]][move[1]] = player
        move_val = minimax(board, 0, player == 'O')
        board[move[0]][move[1]] = ' '

        if player == 'X' and move_val > best_val:
            best_val = move_val
            best_move = move
        elif player == 'O' and move_val < best_val:
            best_val = move_val
            best_move = move

    return best_move

def print_board(board):
    print("  0 1 2")
    for i, row in enumerate(board):
        print(f"{i} {' '.join(row)}")

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def get_valid_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner:
        return {'X': 1, 'O': -1, 'Draw': 0}[winner]
    if is_draw(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for move in get_valid_moves(board):
            board[move[0]][move[1]] = 'X'
            eval = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_valid_moves(board):
            board[move[0]][move[1]] = 'O'
            eval = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board, player):
    best_val = float('-inf') if player == 'X' else float('inf')
    best_move = None

    for move in get_valid_moves(board):
        board[move[0]][move[1]] = player
        move_val = minimax(board, 0, player == 'O')
        board[move[0]][move[1]] = ' '
        if player == 'X' and move_val > best_val:
            best_val = move_val
            best_move = move
        elif player == 'O' and move_val < best_val:
            best_val = move_val
            best_move = move

    return best_move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while not check_winner(board) and not is_draw(board):
        print_board(board)
        if current_player == 'X':
            move = best_move(board, 'X')
            board[move[0]][move[1]] = 'X'
            print(f"AI played: {move[0]} {move[1]}")
        else:
            while True:
                try:
                    move_input = input("Enter your move (row col): ")
                    row, col = map(int, move_input.split())
                    if board[row][col] == ' ':
                        board[row][col] = 'O'
                        break
                    else:
                        print("Invalid move, cell already taken. Try again.")
                except ValueError:
                    print("Invalid input. Please enter row and column numbers separated by a space (e.g., 1 1).")
                except IndexError:
                    print("Invalid move. Row and column should be between 0 and 2. Try again.")

        current_player = 'O' if current_player == 'X' else 'X'

    print_board(board)
    winner = check_winner(board)
    if winner:
        print(f"{winner} wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_game()