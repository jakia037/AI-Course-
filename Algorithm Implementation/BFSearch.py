def bfs(graph, visit, node, queue):
    visit.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for nodes in graph[m]:
            if nodes not in visit:
                visit.append(nodes)
                queue.append(nodes)


graph = {}
n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"Enter node {i+1} name: ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

start = input("Enter starting node: ")

v = []
q = []

print("\nBFS Traversal:")
bfs(graph, v, start, q)

