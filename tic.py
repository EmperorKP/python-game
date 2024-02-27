def print_board(board):
    for row in board:
        print(" ".join(row))

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    if [player, player, player] in win_conditions:
        return True
    return False

def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def tic_tac_toe():
    board = [[' ']*3 for _ in range(3)]
    players = ['X', 'O']

    while True:
        for player in players:
            print_board(board)
            while True:
                row = int(input(f"Player {player}, enter your move's row (1-3): ")) - 1
                col = int(input(f"Player {player}, enter your move's column (1-3): ")) - 1
                if (0 <= row <= 2) and (0 <= col <= 2) and board[row][col] == ' ':
                    board[row][col] = player
                    break
                else:
                    print("Invalid move, try again.")
            if check_win(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                return
            elif check_draw(board):
                print_board(board)
                print("It's a draw!")
                return

tic_tac_toe()
