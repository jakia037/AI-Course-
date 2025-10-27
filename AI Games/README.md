# 🎮 Tic Tac Toe – AI vs Human (Using Minimax Algorithm)

## 🧠 Overview
This project implements the **Tic Tac Toe** game where a **human player** competes against an **AI player**.  
The AI uses the **Minimax Algorithm** to make optimal moves — it never loses!

---

## ⚙️ i. How to Run the File
any o
 Python compiler 


## 🧩 ii. Requirements

No special libraries are required — this program runs with default Python.

✅ Pre-installed needed:
Python 3.7 or above
(for GUI version):
tkinter (comes by default with Python)

## 🎮 iii. How to Play

The game board is a 3x3 grid.
You play as ‘O’, and the computer plays as ‘X’.
Choose your move by entering a number corresponding to a cell (1–9).
The AI instantly responds with its move using the Minimax Algorithm.
The game continues until:
You or the AI wins 🎉
Or the board fills up (Draw 🤝)

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
🔹 How It Works
The AI builds a search tree of possible moves up to a fixed search depth.
At terminal nodes (or when depth limit reached), the board is evaluated using a heuristic evaluation function that scores material balance, piece-square tables, mobility, king safety, etc.
The Minimax algorithm assumes both players play optimally:
Maximizer (AI when playing as White) seeks to maximize evaluation.
Minimizer (opponent) seeks to minimize evaluation.
Alpha-Beta Pruning cuts off branches that cannot possibly influence the final decision (when beta <= alpha), improving performance while returning the same optimal move as plain Minimax.

# 🪨 Nim Game – AI vs Human (Using Minimax Algorithm)

## 🧠 Overview
The **Nim Game** is a mathematical strategy game where players take turns removing 1 to *n* stones from a pile.  
The player forced to take the **last stone loses** (in this version).  
The **AI uses the Minimax Algorithm** to make optimal moves, ensuring that it always plays perfectly and can’t be easily beaten.

---

## ⚙️ i. How to Run the File
You can run the Nim Game file in **any Python environment** that supports `tkinter`.

### 🧩 Steps:
1. Save your file as `nim_game.py`.
2. Make sure you have **Python 3.7 or higher** installed.
3. Run the file from your terminal or command prompt:
   ```bash
   python nim_game.py
## 🧩 ii. Requirements
Pre-installed Library:
tkinter (comes by default with Python)
Python Version:
Python 3.7 or above
No external dependencies or frameworks are needed.

## 🎮 iii. How to Play
The game starts with 15 stones (default).
Each player can take 1, 2, or 3 stones per turn.
You play first (human).
The AI calculates its best move using the Minimax Algorithm.
Whoever takes the last stone loses!

🟢 Your Turn: Click the button labeled Take 1, Take 2, or Take 3.
🔴 AI Turn: Wait for the message “AI is thinking…” — it will automatically make its move after 1 second.
🎉 Game ends when all stones are taken.

## 🧠 iv. Algorithm Used – Minimax Algorithm
🔹 How It Works

The Minimax Algorithm is used for decision-making in turn-based games.
It simulates all possible future moves to determine the optimal move that guarantees the best possible outcome against an optimal opponent.

🔹 AI Logic (Simplified)

The AI recursively explores all possible stone removal choices.
Each move is evaluated as a win (+1) or loss (-1).
The AI selects the move that maximizes its chances of winning (assuming the player plays perfectly too).


