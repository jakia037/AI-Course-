## How it works:

- DFS explores as far as possible along each branch before backtracking.
- Uses either recursion (like above) or a stack explicitly.
- Good for: pathfinding, topological sort, cycle detection.

## Complexity:

- Time: O(V + E) — each node and edge is visited once.
- Space: O(V) — recursion stack or explicit stack + visited set.
