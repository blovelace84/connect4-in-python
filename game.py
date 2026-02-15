ROWS = 6
COLS = 7

# Create board
board = [[ " "for _ in range(COLS)] for _ in range(ROWS)]

def print_board():
    print("\n")
    for row in board:
        print("|" + "|".join(row) + "|")
    print("-" * (COLS * 2 + 1))
    print("-" + " ".join(str(i) for i in range(COLS)))

def drop_piece(col, piece):
    for row in reversed(range(ROWS)):
        if board[row][col] == " ":
            board[row][col] = piece
            return row
        return None
    return None


def check_win(piece):
    # Horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c+i] == piece for i in range(4)):
                return True


    # Vertical
    for r in range(ROWS - 3):
        for c in range(COLS):
            if all(board[r+i][c] == piece for i in range(4)):
                return True

        # Diagonal /
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r - i][c + i] == piece for i in range(4)):
                return True

        # Diagonal \
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r + i][c + i] == piece for i in range(4)):
                return True

    return False

def board_ful():
    return all(board[0][c] != " " for c in range(COLS))

# Game Loop
player = 1
pieces = {1: "X", 2: "0"}


def board_full():
    pass


while True:
    print_board()
    col = int(input(f"Player {player} ({pieces[player]}), choose column 0-6: "))

    if col < 0 or col >= COLS:
        print("Invalid column")
        continue

    row = drop_piece(col, pieces[player])
    if row is None:
        print("Column full.")
        continue

    if check_win(pieces[player]):
        print(f"Player {player} wins!")
        break

    if board_full():
        print_board()
        print("Draw!")
        break

    player = 2 if player == 1 else 1