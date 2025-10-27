import tkinter as tk
from tkinter import messagebox
import math

# -------------------- Initial Board Setup --------------------
start_board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]

# -------------------- Piece Symbols --------------------
symbols = {
    "r": "♜", "n": "♞", "b": "♝", "q": "♛", "k": "♚", "p": "♟",
    "R": "♖", "N": "♘", "B": "♗", "Q": "♕", "K": "♔", "P": "♙"
}

# -------------------- Piece Values --------------------
piece_values = {'p': 1, 'n': 3, 'b': 3, 'r': 5, 'q': 9, 'k': 100}

# -------------------- Move Piece --------------------
def make_move(board, r1, c1, r2, c2):
    """Move a piece from (r1,c1) to (r2,c2)"""
    piece = board[r1][c1]
    board[r1][c1] = '.'
    board[r2][c2] = piece

    # Pawn promotion
    if piece == 'P' and r2 == 0:
        board[r2][c2] = 'Q'
    if piece == 'p' and r2 == 7:
        board[r2][c2] = 'q'
    return board

# -------------------- Evaluate Board --------------------
def evaluate_board(board):
    """Return total score of current board"""
    score = 0
    for row in board:
        for p in row:
            if p != '.':
                value = piece_values[p.lower()]
                score += value if p.isupper() else -value
    return score

# -------------------- Get Piece Moves --------------------
def get_piece_moves(board, row, col):
    """Generate all possible moves for a given piece"""
    moves = []
    piece = board[row][col]
    if piece == '.':
        return moves
    directions = []

    if piece.lower() == 'p':  # Pawn
        step = -1 if piece.isupper() else 1
        start_row = 6 if piece.isupper() else 1
        if 0 <= row + step < 8 and board[row + step][col] == '.':
            moves.append((row + step, col))
            if row == start_row and board[row + 2 * step][col] == '.':
                moves.append((row + 2 * step, col))
        for dc in [-1, 1]:
            if 0 <= col + dc < 8 and 0 <= row + step < 8:
                target = board[row + step][col + dc]
                if target != '.' and target.isupper() != piece.isupper():
                    moves.append((row + step, col + dc))

    elif piece.lower() == 'n':  # Knight
        for dr, dc in [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                t = board[r][c]
                if t == '.' or t.isupper() != piece.isupper():
                    moves.append((r, c))

    elif piece.lower() == 'b':
        directions = [(-1,-1),(-1,1),(1,-1),(1,1)]
    elif piece.lower() == 'r':
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
    elif piece.lower() == 'q':
        directions = [(-1,-1),(-1,1),(1,-1),(1,1),(-1,0),(1,0),(0,-1),(0,1)]
    elif piece.lower() == 'k':
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                if dr==0 and dc==0: continue
                r, c = row+dr, col+dc
                if 0<=r<8 and 0<=c<8:
                    t = board[r][c]
                    if t=='.' or t.isupper()!=piece.isupper():
                        moves.append((r,c))

    if directions:
        for dr, dc in directions:
            r, c = row+dr, col+dc
            while 0<=r<8 and 0<=c<8:
                t = board[r][c]
                if t == '.':
                    moves.append((r,c))
                else:
                    if t.isupper()!=piece.isupper():
                        moves.append((r,c))
                    break
                r+=dr
                c+=dc
    return moves

# -------------------- Check if King is Alive --------------------
def is_king_alive(board, color):
    """Return True if king of given color exists"""
    king = 'K' if color == 'white' else 'k'
    for row in board:
        if king in row:
            return True
    return False

# -------------------- Minimax + Alpha-Beta --------------------
def minimax(board, depth, alpha, beta, maximizing):
    """Minimax with alpha-beta pruning"""
    if depth == 0:
        return evaluate_board(board), None

    best_move = None
    if maximizing:  # White (Human)
        max_eval = -math.inf
        for r in range(8):
            for c in range(8):
                p = board[r][c]
                if p.isupper():
                    for (mr, mc) in get_piece_moves(board, r, c):
                        copy = [row[:] for row in board]
                        make_move(copy, r, c, mr, mc)
                        eval_score, _ = minimax(copy, depth-1, alpha, beta, False)
                        if eval_score > max_eval:
                            max_eval = eval_score
                            best_move = (r, c, mr, mc)
                        alpha = max(alpha, eval_score)
                        if beta <= alpha:
                            break
        return max_eval, best_move

    else:  # Black (AI)
        min_eval = math.inf
        for r in range(8):
            for c in range(8):
                p = board[r][c]
                if p.islower():
                    for (mr, mc) in get_piece_moves(board, r, c):
                        copy = [row[:] for row in board]
                        make_move(copy, r, c, mr, mc)
                        eval_score, _ = minimax(copy, depth-1, alpha, beta, True)
                        if eval_score < min_eval:
                            min_eval = eval_score
                            best_move = (r, c, mr, mc)
                        beta = min(beta, eval_score)
                        if beta <= alpha:
                            break
        return min_eval, best_move

# -------------------- GUI Class --------------------
class ChessGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("♟ Chess AI (Minimax + Alpha-Beta) ♛")
        self.board = [r[:] for r in start_board]
        self.selected = None
        self.size = 80
        self.canvas = tk.Canvas(root, width=8*self.size, height=8*self.size)
        self.canvas.pack()
        self.draw_board()
        self.canvas.bind("<Button-1>", self.on_click)

    def draw_board(self):
        """Draw the chess board and pieces"""
        self.canvas.delete("all")
        for r in range(8):
            for c in range(8):
                color = "#f0d9b5" if (r + c) % 2 == 0 else "#b58863"
                x1, y1 = c * self.size, r * self.size
                x2, y2 = x1 + self.size, y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
                piece = self.board[r][c]
                if piece != '.':
                    text_color = "black" if piece.isupper() else "white"
                    self.canvas.create_text(
                        x1 + self.size / 2, y1 + self.size / 2,
                        text=symbols[piece], font=("DejaVu Sans", 48),
                        fill=text_color
                    )

        if self.selected:
            sr, sc = self.selected
            self.canvas.create_rectangle(sc*self.size, sr*self.size,
                                         (sc+1)*self.size, (sr+1)*self.size,
                                         outline="red", width=3)

    def on_click(self, event):
        """Handle human player's mouse clicks"""
        r, c = event.y // self.size, event.x // self.size
        if r < 0 or r > 7 or c < 0 or c > 7:
            return
        if self.selected:
            sr, sc = self.selected
            if (r, c) in get_piece_moves(self.board, sr, sc):
                make_move(self.board, sr, sc, r, c)
                self.selected = None
                self.draw_board()

                # Check if AI king is dead
                if not is_king_alive(self.board, 'black'):
                    messagebox.showinfo("Game Over", "You Win! 🎉")
                    self.root.quit()

                self.root.after(500, self.ai_move)
            else:
                self.selected = None
                self.draw_board()
        else:
            if self.board[r][c].isupper():
                self.selected = (r, c)
                self.draw_board()

    def ai_move(self):
        """AI's move using minimax"""
        _, move = minimax(self.board, 2, -math.inf, math.inf, False)
        if move:
            sr, sc, er, ec = move
            make_move(self.board, sr, sc, er, ec)
            self.draw_board()

            # Check if human king is dead
            if not is_king_alive(self.board, 'white'):
                messagebox.showinfo("Game Over", "AI Wins! 🤖")
                self.root.quit()

# -------------------- Run App --------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ChessGUI(root)
    root.mainloop()
