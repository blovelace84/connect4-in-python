from flask import Flask, render_template, redirect

app = Flask(__name__)

ROWS = 6
COLS = 7
board = [[""]*COLS for _ in range(ROWS)]
winner = None
player = 1

def drop_piece(col):
    global player, winner

    if winner:
        return

    for r in reversed(range(ROWS)):
        if board[r][col] == "":
            piece = "X" if player == 1 else "0"
            board[r][col] = piece

            if check_win(piece):
                winner = f"player {player} wins!"

            player = 2 if player == 1 else 1
            break

def check_win(piece):
    # Horizontal
    for r in range(ROWS):
        for c in range(COLS):
            if all(board[r][c+i] == piece for i in range(3)):
                return True

    # Vertical
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True

    # Diagonal \
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True

    # Diagonal /
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True

    return False
@app.route('/')
def home():
    return render_template("index.html", board=board, winner=winner)

@app.route("/move/<int:col>")
def move(col):
    drop_piece(col)
    return redirect("/")

@app.route("/reset")
def reset():
    global board, player
    board = [[""]*COLS for _ in range(ROWS)]
    player = 1
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)