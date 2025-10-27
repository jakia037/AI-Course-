# ♟️ Chess – AI vs Human (Minimax with Alpha-Beta Pruning)

## 🧠 Overview
This project implements a simplified **Chess** engine where a **human player** can play against an **AI player**.  
The AI uses the **Minimax algorithm** with **Alpha-Beta Pruning** to evaluate moves and choose the best strategy within a search depth limit.

---

## ⚙️ i. How to Run the File
You can run the chess program in any Python environment that supports the provided files.

### 🧩 If You’re Using Python Locally:
1. Clone or download this repository:
   ```bash
   git clone https://github.com/your-username/AI-Course.git

cd "AI-Course/AI Games/Chess"
Run the main program:
python chess_gui.py

## 🧩 ii. Requirements
This implementation aims to work with default Python, but depending on which version you use, there may be optional dependencies.
✅ Required:
Python 3.7 or above
(for GUI or improved visuals):
pygame (for graphical interface)

## 🎮 iii. How to Play

The board uses standard 8×8 chess notation (ranks 1–8 and files a–h).
You may choose to play as White (moves first) or Black.
Input moves in algebraic or coordinate format, depending on the program version, for example:
Coordinate format: e2e4 (move piece from e2 to e4)
Algebraic: Nf3 (if supported)
After you make a move, the AI will compute its response using Minimax + Alpha-Beta within the configured search depth.
The game continues until:
Checkmate (one player wins) ♟️
Stalemate or draw conditions (threefold repetition, fifty-move rule, insufficient material) 🤝

## 🧠 v. Algorithm Used – Minimax with Alpha-Beta Pruning
## 🔹 How It Works

The AI builds a search tree of possible moves up to a fixed search depth.
At terminal nodes (or when depth limit reached), the board is evaluated using a heuristic evaluation function that scores material balance, piece-square tables, mobility, king safety, etc.
The Minimax algorithm assumes both players play optimally:
Maximizer (AI when playing as White) seeks to maximize evaluation.
Minimizer (opponent) seeks to minimize evaluation.
Alpha-Beta Pruning cuts off branches that cannot possibly influence the final decision (when beta <= alpha), improving performance while returning the same optimal move as plain Minimax.
