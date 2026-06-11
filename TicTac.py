board = [' ' for _ in range(9)]

def print_board():
    print()
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
    print()

def check_win(player):

    wins = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True

    return False

def board_full():
    return ' ' not in board


current_player = 'X'

while True:

    print_board()

    pos = int(input(f"Player {current_player}, enter position (1-9): "))

    if pos < 1 or pos > 9:
        print("Invalid position!")
        continue

    if board[pos - 1] != ' ':
        print("Position already taken!")
        continue

    board[pos - 1] = current_player

    if check_win(current_player):
        print_board()
        print(f"Player {current_player} Wins!")
        break

    if board_full():
        print_board()
        print("Match Draw!")
        break

    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'