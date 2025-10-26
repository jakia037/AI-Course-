import heapq

# Best First Search Algorithm


def best_first_search(graph, heuristic, start, goal):
    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start, [start]))

    while priority_queue:
        cost, current, path = heapq.heappop(priority_queue)

        if current == goal:
            return path

        if current not in visited:
            visited.add(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (heuristic[neighbor], neighbor, path + [neighbor]))

    return None


# ---------------- User Input Section ----------------
graph = {}
n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input(f"Enter node {i+1}: ")
    neighbors = input(f"Enter neighbors of {node} separated by space: ").split()
    graph[node] = neighbors

heuristic = {}
print("\nEnter heuristic values for each node:")
for node in graph:
    h = int(input(f"Heuristic value for {node}: "))
    heuristic[node] = h

start = input("\nEnter Start Node: ")
goal = input("Enter Goal Node: ")

path = best_first_search(graph, heuristic, start, goal)

print("\nPath found using Best First Search:")
print(" -> ".join(path) if path else "No path found")
  
