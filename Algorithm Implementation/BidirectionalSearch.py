from collections import deque

# Bidirectional Search Algorithm


def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    queue_start = deque([start])
    queue_goal = deque([goal])
    visited_start = {start}
    visited_goal = {goal}
    parent_start = {start: None}
    parent_goal = {goal: None}

    while queue_start and queue_goal:
        node = queue_start.popleft()
        for n in graph.get(node, []):
            if n not in visited_start:
                visited_start.add(n)
                parent_start[n] = node
                queue_start.append(n)
            if n in visited_goal:
                return construct_path(parent_start, parent_goal, n)

        node = queue_goal.popleft()
        for n in graph.get(node, []):
            if n not in visited_goal:
                visited_goal.add(n)
                parent_goal[n] = node
                queue_goal.append(n)
            if n in visited_start:
                return construct_path(parent_start, parent_goal, n)
    return None

def construct_path(p_start, p_goal, meet):
    path = []
    node = meet
    while node:
        path.append(node)
        node = p_start[node]
    path.reverse()
    node = p_goal[meet]
    while node:
        path.append(node)
        node = p_goal[node]
    return path

# --------- User Input ---------
graph = {}
n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input(f"Node {i+1} name: ")
    neighbors = input(f"Neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

start = input("Enter start node: ")
goal = input("Enter goal node: ")

path = bidirectional_search(graph, start, goal)
if path:
    print("Path found:", " -> ".join(path))
else:
    print("No path exists")
              
