from collections import deque

# BFS Algorithm (using deque)


def bfs(graph, visit, node, queue):
    visit.append(node)
    queue.append(node)

    while queue:
        m = queue.popleft()
        print(m, end=" ")

        for nodes in graph[m]:
            if nodes not in visit:
                visit.append(nodes)
                queue.append(nodes)


# -------- User Input --------
graph = {}
n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"Enter node {i+1} name: ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

start = input("Enter starting node: ")

v = []
q = deque()

print("\nBFS Traversal:")
bfs(graph, v, start, q)

