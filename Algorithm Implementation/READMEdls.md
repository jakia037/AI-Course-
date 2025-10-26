# DLS Algorithm

## How it works
Depth-Limited Search (DLS) explores a graph depth-first but stops when a predefined depth limit is reached.

## Applications
- Pathfinding with depth constraints
- Solving puzzles like maze or chess moves
- AI search in limited-depth trees

## Complexity
- Time: O(b^l), where b = branching factor, l = depth limit
- Space: O(l) (stack space due to recursion)
