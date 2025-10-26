# 🎮 Minimax Algorithm

## 🔹 How it works
The **Minimax Algorithm** is a decision-making algorithm used in two-player games like Chess or Tic-Tac-Toe.  
It assumes:
- One player tries to **maximize** the score (Maximizer)
- The other tries to **minimize** the score (Minimizer)

The algorithm recursively explores all possible moves and outcomes, evaluating which move gives the **best guaranteed result** for the maximizing player, assuming the opponent plays optimally.

---

## 🔹 Applications
- Game AI (Chess, Tic-Tac-Toe, Connect Four)
- Decision making in adversarial environments
- Pathfinding with opponent interference

---

## 🔹 Complexity
- **Time:** O(b^d)  
  (b = branching factor, d = depth of the tree)
- **Space:** O(b × d)

---
