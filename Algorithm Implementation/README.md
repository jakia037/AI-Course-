## Breadth First Search Algorithm
## How it works
Breadth-First Search (BFS) explores nodes level by level, starting from the source node.

## Applications
Shortest path in unweighted graphs
Social network analysis
Web crawling
## Complexity
Time: O(V + E)
Space: O(V)

## Depth first search

## How it works:

- DFS explores as far as possible along each branch before backtracking.
- Uses either recursion (like above) or a stack explicitly.
- Good for: pathfinding, topological sort, cycle detection.

## Complexity:

- Time: O(V + E) — each node and edge is visited once.
- Space: O(V) — recursion stack or explicit stack + visited set.


## Depth limited search
## How it works:

- DLS is DFS with a depth limit; it explores nodes along each branch but does not go deeper than the specified limit.
- Uses recursion or a stack, like DFS.
- Useful for large or infinite graphs to prevent infinite traversal.

## Complexity:

- Time: O(b^l) — b = branching factor, l = depth limit
- Space: O(l) — stack depth limited by the depth limit

## Iteretive Deepening Search
## How it works:

- IDS combines BFS and DFS ideas.
- Repeatedly performs Depth-Limited Search (DLS) starting from depth = 0, then 1, 2, and so on, until the goal is found.
- Explores nodes in increasing depth levels like BFS but uses DFS to save memory.

## Complexity:

- Time: O(b^d) — b = branching factor, d = depth of the goal
- Space: O(d) — only needs to store nodes along the current path (like DFS)
- Advantage: Finds the shortest path like BFS but with DFS-level memory efficiency
##MiniMax Algorithm
## How it works:

- Minimax is used in **two-player zero-sum games** (like Tic-Tac-Toe, Chess, etc.).
- One player is the "maximizer" trying to get the highest score, and the other is the "minimizer" trying to get the lowest score.
- The algorithm recursively explores all possible moves:
    1. Maximizer chooses the move with the **maximum** score.
    2. Minimizer chooses the move with the **minimum** score.
- This continues until a terminal state (win, loss, draw) is reached.

## Complexity:

- Time: O(b^m) — b = branching factor, m = maximum depth of the game tree
- Space: O(m) — recursion stack depth
- Can be optimized with **Alpha-Beta pruning** to reduce unnecessary branches.

## Alpha beta prunning

## How it works:

- Alpha-Beta Pruning is an optimization of the Minimax algorithm.
- It **cuts off branches** in the game tree that cannot affect the final decision.
- Uses two values:
    - Alpha (α): the best value that the maximizer can guarantee so far.
    - Beta (β): the best value that the minimizer can guarantee so far.
- During recursion:
    1. If the minimizer finds a value ≤ alpha, prune (stop exploring this branch).
    2. If the maximizer finds a value ≥ beta, prune (stop exploring this branch).
- This reduces the number of nodes evaluated while producing the **same result as Minimax**.

## Complexity:

- Time: O(b^(m/2)) in the best case — effectively doubling the depth you can search.
- Space: O(m) — recursion stack depth
- Maintains optimal decision like Minimax but much faster in practice.

## Beam Search Algorithm
## How it works:

- Beam Search is a **heuristic search algorithm** used in AI and NLP.
- It is like **Breadth-First Search (BFS)** but only keeps the top-k best nodes at each level, where k is called the **beam width**.
- At each step:
    1. Expand all nodes in the current level.
    2. Evaluate nodes using a heuristic or score.
    3. Keep only the top-k nodes for the next level.
- Reduces memory usage compared to BFS by limiting the number of nodes explored.

## Applications:

- Machine translation, speech recognition, text generation, pathfinding in large search spaces.

## Complexity:

- Time: O(b * k * d) — b = branching factor, k = beam width, d = depth
- Space: O(k * d) — only stores top-k nodes at each depth
- Not guaranteed to find the optimal solution but often finds good solutions efficiently.

