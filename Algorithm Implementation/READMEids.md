# IDS Algorithm

## How it works
Iterative Deepening Search (IDS) applies Depth-Limited Search repeatedly with increasing depth limits until the goal node is found.

## Applications
- Pathfinding when goal depth is unknown
- Memory-efficient graph/tree search
- AI puzzle solving with unknown solution depth

## Complexity
- Time: O(b^d), b = branching factor, d = depth of goal
- Space: O(d) (stack space for DFS)
