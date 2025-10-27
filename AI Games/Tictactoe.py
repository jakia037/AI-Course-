import tkinter as tk
import math

# Evaluate the board
def evaluate(board):
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "":
            return 10 if row[0] == "O" else -10
    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            return 10 if board[0][col] == "O" else -10
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return 10 if board[0][0] == "O" else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return 10 if board[0][2] == "O" else -10
    return 0

# Check if moves left
def is_moves_left(board):
    for row in board:
        if "" in row:
            return True
    return False

# Minimax
def minimax(board, depth, is_max):
    score = evaluate(board)
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "O"
                    best = max(best, minimax(board, depth+1, False))
                    board[i][j] = ""
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "X"
                    best = min(best, minimax(board, depth+1, True))
                    board[i][j] = ""
        return best

# Best move
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "O"
                move_val = minimax(board, 0, False)
                board[i][j] = ""
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move

# Main UI
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Human (X) vs AI (O)")
        self.board = [[""]*3 for _ in range(3)]
        self.buttons = [[None]*3 for _ in range(3)]

        for i in range(3):
            for j in range(3):
                btn = tk.Button(root, text="", font=("Arial", 32), width=5, height=2,
                                command=lambda r=i, c=j: self.player_move(r, c))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

    def player_move(self, i, j):
        if self.board[i][j] == "" and evaluate(self.board) == 0:
            self.board[i][j] = "X"
            self.buttons[i][j].config(text="X", state="disabled")
            if evaluate(self.board) == -10:
                self.end_game("You win!")
                return
            if not is_moves_left(self.board):
                self.end_game("It's a draw!")
                return

            # AI move
            ai_i, ai_j = find_best_move(self.board)
            if ai_i != -1 and ai_j != -1:
                self.board[ai_i][ai_j] = "O"
                self.buttons[ai_i][ai_j].config(text="O", state="disabled")

            score = evaluate(self.board)
            if score == 10:
                self.end_game("AI wins!")
            elif not is_moves_left(self.board):
                self.end_game("It's a draw!")

    def end_game(self, result):
        popup = tk.Toplevel(self.root)
        popup.title("Game Over")
        tk.Label(popup, text=result, font=("Arial", 20)).pack(pady=10)
        tk.Button(popup, text="Play Again", command=lambda: [popup.destroy(), self.reset_board()]).pack(pady=5)
        tk.Button(popup, text="Exit", command=self.root.destroy).pack(pady=5)

    def reset_board(self):
        self.board = [[""]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
