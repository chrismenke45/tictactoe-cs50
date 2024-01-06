"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    empty_count = 0
    for row in board:
        empty_count += row.count(EMPTY)
    return X if empty_count % 2 == 1 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_spaces = set()
    # i is row, j is column
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY: 
                empty_spaces.add((i, j))
    return empty_spaces


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise ValueError("action is not allowed on the board")
    current_player = player(board)
    boardCopy = list(map(lambda x: x.copy(), board))
    boardCopy[action[0]][action[1]] = current_player
    return boardCopy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # horizontal
    for row in board:
        if row.count(row[0]) == len(row):
            if row[0] != EMPTY:
                return row[0]
            
    # vertical     
    for column in range(len(board[0])):
        if board[0][column] == board[1][column] and board[0][column] == board[2][column]:
            if board[0][column] != EMPTY:
                return board[0][column]
    
    # left diagonal
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        if board[0][0] != EMPTY:
                return board[0][0]
        
    # right diagonal
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        if board[0][2] != EMPTY:
                return board[0][2]
    
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    
    empty_count = 0
    for row in board:
        empty_count += row.count(EMPTY)
    
    return empty_count == 0


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    who_won = winner(board)
    if who_won == X:
        return 1
    elif who_won == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    def max_value(state):
        if terminal(state):
            return utility(state)
        v_max = -math.inf
        for action in actions(state):

            v_max = max(v_max, min_value(result(state, action)))
            if v_max == 1:
                #print("break in max")
                break
        return v_max

    def min_value(state):
        if terminal(state):
            return utility(state)
        v_min = math.inf
        for action in actions(state):
            v_min = min(v_min, max_value(result(state, action)))
            if v_min == -1:
                break
        return v_min
    
    possible_moves = actions(board)
    if player(board) == X:
        main_v = -math.inf
        for possible_move in possible_moves:
            move_value = min_value(result(board, possible_move))
            if move_value > main_v:
                main_v = move_value
                move_to_make = possible_move
                if main_v == 1:
                    break
    else:
        main_v = math.inf
        for possible_move in possible_moves:
            move_value = max_value(result(board, possible_move))
            if move_value < main_v:
                main_v = move_value
                move_to_make = possible_move
                if main_v == -1:
                    break
    return move_to_make
