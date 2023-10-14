import numpy as np
import random
def create_board():
    return np.zeros((3, 3))
def check_win(board, player):
    for row in board:
        if np.all(row == player):
            return True

    for col in range(3):
        if np.all(board[:, col] == player):
            return True

    if np.all(board[::-1, :] == player):
        return True

    if np.all(board[:, ::-1] == player):
        return True

    return False
def check_draw(board):
    return np.all(board != 0) and not check_win(board, 1) and not check_win(board, -1)
def make_move(board, row, col, player):
    if board[row, col] == 0:
        board[row, col] = player
        return True
    return False
def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or check_win(board, 1) or check_win(board, -1) or check_draw(board):
        return evaluate_board(board)

    if maximizing_player:
        max_eval = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row, col] == 0:
                    board[row, col] = 1
                    eval = minimax(board, depth - 1, alpha, beta, False)
                    board[row, col] = 0
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
