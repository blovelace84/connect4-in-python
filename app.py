from flask import Flask, render_template, redirect

app = Flask(__name__)

ROWS = 6
COLS = 7
board = [[" "]*COLS for _ in range(ROWS)]
player = 1

def drop_piece(col):
    global player
    for r in reversed(range(ROWS)):
        if board[r][col] == " ":
            board[r][col] =  "X" if player == 1 else "0"
            player = 2 if player == 1 else 1
            break

@app.route('/')
def home():
    return render_template("index.html", board=board)

@app.route("/move/<int:col>")
def move(col):
    drop_piece(col)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)