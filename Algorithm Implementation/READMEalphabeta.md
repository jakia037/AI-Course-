# 🤖 Alpha-Beta Pruning Algorithm

## 🔹 How it Works
The **Alpha-Beta Pruning Algorithm** is an optimized version of the **Minimax Algorithm** used in two-player games.  
It eliminates branches in the game tree that **cannot possibly affect the final decision**, improving efficiency without changing the result.

- **Alpha (α):** The best value the maximizing player can guarantee so far.  
- **Beta (β):** The best value the minimizing player can guarantee so far.  
- If at any node **β ≤ α**, the remaining branches are **pruned** (skipped) because they will never influence the final choice.

**Process Overview:**
1. Start from the root node and apply the Minimax logic recursively.  
2. Track the best (α) and worst (β) possible values at each level.  
3. Stop exploring further when the pruning condition (β ≤ α) occurs.  
4. Return the same optimal value as Minimax, but with fewer computations.

---

## 🔹 Applications
- Used in **Game AI** (Chess, Tic-Tac-Toe, Checkers, Connect Four)  
- Decision-making systems involving **two opposing agents**  
- **Search optimization** where reducing time complexity is essential  

---

## 🔹 Complexity
- **Time Complexity:** O(bᵈ) in worst case, O(b^(d/2)) in best case  
  (b = branching factor, d = depth of the tree)  
- **Space Complexity:** O(b × d)

---

