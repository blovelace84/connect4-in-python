import tkinter as tk

ROWS = 6
COLS = 7

board = [[" "]*COLS for _ in range(ROWS)]
player = 1
pieces = {1: "X", 2: "O"}

def drop_piece(col):
    global player

    for r in reversed(range(ROWS)):
        if board[r][col] == " ":
            board[r][col] = pieces[player]
            labels[r][col]["text"] = pieces[player]

            if check_win(pieces[player]):
                status.config(text=f"Player {player} wins!")
                disable_buttons()
                return

            player = 2 if player == 1 else 1
            status.config(text=f"Player {player}'s turn")
            return

def disable_buttons():
    for b in buttons:
        b.config(state="disabled")

def check_win(piece):
    # horizontal
    for r in range(ROWS):
        for c in range(COLS-3):
            if all(board[r][c+i]==piece for i in range(4)):
                return True

    # vertical
    for r in range(ROWS-3):
        for c in range(COLS):
            if all(board[r+i][c]==piece for i in range(4)):
                return True

    # diag \
    for r in range(ROWS-3):
        for c in range(COLS-3):
            if all(board[r+i][c+i]==piece for i in range(4)):
                return True

    # diag /
    for r in range(3,ROWS):
        for c in range(COLS-3):
            if all(board[r-i][c+i]==piece for i in range(4)):
                return True

    return False

root = tk.Tk()
root.title("Connect 4")

status = tk.Label(root, text="Player 1's turn", font=("Arial", 14))
status.grid(row=0, column=0, columnspan=COLS)

buttons = []
for c in range(COLS):
    b = tk.Button(root, text="↓", font=("Arial", 14),
                  command=lambda c=c: drop_piece(c))
    b.grid(row=1, column=c)
    buttons.append(b)

labels = []
for r in range(ROWS):
    row = []
    for c in range(COLS):
        l = tk.Label(root, text=" ", width=4, height=2,
                     borderwidth=2, relief="ridge",
                     font=("Arial", 18))
        l.grid(row=r+2, column=c)
        row.append(l)
    labels.append(row)

root.mainloop()
