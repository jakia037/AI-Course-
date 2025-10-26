#DLSAlgorithm

def dls(graph, visit, node, limit, depth=0, goal=None):
    if depth > limit:
        return False
    
    visit.append(node)
    print(node, end=" ")

    if node == goal:
        return True

    for neighbor in graph[node]:
        if neighbor not in visit:
            found = dls(graph, visit, neighbor, limit, depth+1, goal)
            if found:
                return True

    return False


graph = {}
n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"Enter node {i+1} name: ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

start = input("Enter start node: ")
goal = input("Enter goal node: ")
limit = int(input("Enter depth limit: "))

v = []
print("\nTraversal Order: ", end="")
found = dls(graph, v, start, limit, 0, goal)

if found:
    print(f"\nGoal '{goal}' found within depth limit {limit}")
else:
    print(f"\nGoal '{goal}' not found within depth limit {limit}")
