import math

HUMAN_PLAYER = 'X'
AI_PLAYER = 'O'
EMPTY = ' '

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_win(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
                all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
            all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False
def is_board_full(board):
    return all([cell != EMPTY for row in board for cell in row])

def evaluate(board):
    if check_win(board, AI_PLAYER):
        return 1
    elif check_win(board, HUMAN_PLAYER):
        return -1
    else:
        return 0
def minimax(board, depth, alpha, beta, is_maximizing):
    score = evaluate(board)
    if score != 0 or depth == 0 or is_board_full(board):
        return score

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI_PLAYER
                    eval = minimax(board, depth - 1, alpha, beta, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN_PLAYER
                    eval = minimax(board, depth - 1, alpha, beta, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval
def ai_move(board):
    best_eval = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI_PLAYER
                eval = minimax(board, 3, -math.inf, math.inf, False)
                board[i][j] = EMPTY
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move
def main():
    board = [[EMPTY] * 3 for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        while True:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == EMPTY:
                board[row][col] = HUMAN_PLAYER
                break
            else:
                print("Invalid move. Try again.")
        print_board(board)

        if check_win(board, HUMAN_PLAYER):
            print("You win!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        row, col = ai_move(board)
        board[row][col] = AI_PLAYER
        print("AI's move:")
        print_board(board)

        if check_win(board, AI_PLAYER):
            print("AI wins!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break
if __name__ == "__main__":
    main()
