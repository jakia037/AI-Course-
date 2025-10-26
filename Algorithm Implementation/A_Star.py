import heapq   # Priority queue for efficient node selection

# -------------------------------------
# 🚀 A* Search Algorithm
# -------------------------------------



def a_star_search(graph, heuristics, start, goal):
    # Priority queue contains tuples: (f, node, path, g)
    pq = [(heuristics[start], start, [start], 0)]
    visited = set()

    while pq:
        f, node, path, g = heapq.heappop(pq)   # Pop lowest f(n)

        if node in visited:
            continue
        visited.add(node)

        # Goal test
        if node == goal:
            return path, g

        # Explore neighbors
        for neighbor, cost in graph.get(node, []):
            if neighbor not in visited:
                g_new = g + cost                  # new path cost
                f_new = g_new + heuristics[neighbor]  # f = g + h
                heapq.heappush(pq, (f_new, neighbor, path + [neighbor], g_new))

    # If goal not found
    return None, float("inf")


# -------------------------------
# 🧩 User Input Section
# -------------------------------
graph = {}
heuristics = {}

n = int(input("Enter number of nodes: "))

# Input heuristic values and initialize empty adjacency list
for _ in range(n):
    node = input("Enter node name: ")
    h = int(input(f"Enter heuristic value for {node}: "))
    heuristics[node] = h
    graph[node] = []

# Input edges
e = int(input("Enter number of edges: "))
for _ in range(e):
    u = input("From node: ")
    v = input("To node: ")
    cost = int(input(f"Enter cost for {u} -> {v}: "))
    graph[u].append((v, cost))

start = input("Enter Start node: ")
goal = input("Enter Goal node: ")

# Run A* Search
path, cost = a_star_search(graph, heuristics, start, goal)

# ---------------------------------
# 🖥️ Output
# ----------------------------------
if path:
    print("\n A* Path found:", " -> ".join(path))
    print("Total cost =", cost)
else:
    print("\n No path found.")
  
