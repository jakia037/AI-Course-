# A* (A-Star) Search Algorithm

## 🔹 How It Works
A* Search is an informed search algorithm that combines the benefits of **Uniform Cost Search** and **Greedy Best-First Search**.  
It evaluates nodes using the function:
f(n) = g(n) + h(n)


- `g(n)` = cost from start node to current node  
- `h(n)` = estimated cost from current node to goal (heuristic)

It always expands the node with the smallest total cost `f(n)`.

---

## 🔹 Applications
- GPS Navigation Systems
- Robotics Path Planning
- Game AI (pathfinding)
- Network Routing
- Puzzle Solving (like 8-puzzle, 15-puzzle)

---

## 🔹 Complexity
- **Time:** O(E log V)
- **Space:** O(V)
