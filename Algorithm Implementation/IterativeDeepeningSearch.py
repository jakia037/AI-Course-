# IDS Algorithm


def dls(graph, node, goal, limit, depth=0, visit=None):
    if visit is None:
        visit = []

    if depth > limit:
        return visit

    visit.append(node)

    if node == goal:
        return visit

    for neighbor in graph[node]:
        if neighbor not in visit:
            visit = dls(graph, neighbor, goal, limit, depth + 1, visit)
    
    return visit

# ---------- User Input ----------
graph = {}
n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"Enter node {i+1} name: ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

start = input("Enter start node: ")
goal = input("Enter goal node: ")
max_depth = int(input("Enter maximum depth to try: "))

# ---------- IDS ----------
for depth in range(max_depth + 1):
    visit = []
    visit = dls(graph, start, goal, depth)
    print(f"{depth+1}th iteration (Depth limit={depth}): {' '.join(visit)}")
    if goal in visit:
        print(f"Goal '{goal}' found at depth {depth}")
        break
else:
    print(f"Goal '{goal}' not found within depth {max_depth}")
    
