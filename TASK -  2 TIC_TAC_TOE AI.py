import math # import math module for infinity values

# Constants for players
HUMAN = 'O' # human player symbol
AI = 'X' # ai player symbol 
EMPTY = ' ' # empty cell symbol

# Initialize board
def create_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)] # create a  empty 3x3 list filled 

# Display board properly
def print_board(board):
    print("\n  0   1   2") # print column headers
    for idx, row in enumerate(board): loop through each row with index
        print(f"{idx} {' | '.join(row)}") # print row with separator
        if idx < 2:
            print("  ---------") # print horizontal separator between rows
    print()

# Check for a winner or draw
def check_winner(board):
    lines = (
        # Rows and columns
        *board,
        *[[board[r][c] for r in range(3)] for c in range(3)], # all columns
        # Diagonals
        [board[i][i] for i in range(3)], # main
        [board[i][2 - i] for i in range(3)] # anti
    )
    if [AI] * 3 in lines:
        return AI # ai wins
    if [HUMAN] * 3 in lines:
        return HUMAN # human wins
    if all(cell != EMPTY for row in board for cell in row):
        return 'Draw' # when no empty cells
    return None # no result

# Get list of valid (empty) positions
def available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == EMPTY]

# Minimax algorithm with Alpha-Beta pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board) # check if game is over
    if winner == AI:
        return 10 - depth # favor faster ai wins
    if winner == HUMAN:
        return depth - 10 # favor slower human wins
    if winner == 'Draw':
        return 0 # neutral score for draw

    if is_maximizing: # ai aims to maximixe score
        max_eval = -math.inf
        for (r, c) in available_moves(board):
            board[r][c] = AI # try ai move
            eval = minimax(board, depth + 1, False, alpha, beta) # recurse with human turn
            board[r][c] = EMPTY # undo move
            max_eval = max(max_eval, eval) # choose max score
            alpha = max(alpha, eval) #update alpha
            if beta <= alpha:
                break # prune branch
        return max_eval
    else: # human aims to manimize score
        min_eval = math.inf 
        for (r, c) in available_moves(board):
            board[r][c] = HUMAN # try human move
            eval = minimax(board, depth + 1, True, alpha, beta) # recurse with ai turn
            board[r][c] = EMPTY # undo moves
            min_eval = min(min_eval, eval) # choose min score
            beta = min(beta, eval) # update beta
            if beta <= alpha:
                break # prune branch
        return min_eval

# Find best move for AI
def best_move(board):
    best_score = -math.inf
    move = None
    for (r, c) in available_moves(board): # try all empty cells
        board[r][c] = AI # simulate ai mopves
        score = minimax(board, 0, False, -math.inf, math.inf) # evaluate move
        board[r][c] = EMPTY # undo move
        if score > best_score:  # update best move
            best_score = score
            move = (r, c)
    return move # return optimal move

# Human move input
def human_move(board):
    while True:
        try:
            row = int(input("Enter row (0-2): ")) # ask for row select
            col = int(input("Enter column (0-2): ")) # ask for col,umn select
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == EMPTY:
                return (row, col) # valid move
            else:
                print("Invalid or occupied cell. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter numbers from 0 to 2.")

# Main game loop
def play_game():
    board = create_board() # create empty board
    print("Welcome to Tic-Tac-Toe!")
    print("You're 'O'. AI is 'X'.") # assign symbols
    print_board(board) # show initial board

    current_player = HUMAN # human starts first

    while True:
        if current_player == HUMAN:
            row, col = human_move(board) # get human move
        else:
            print("AI is thinking...")
            row, col = best_move(board)  # get best ai move

        board[row][col] = current_player #apply move
        print_board(board) # show updated board

        result = check_winner(board) # check for win/draw
        if result:
            if result == 'Draw':
                print("It's a draw!") # Game is a draw
            else:
                print(f"{'AI' if result == AI else 'You'} won the game!") # announce winner
            break

        current_player = AI if current_player == HUMAN else HUMAN # switch turns

play_game()