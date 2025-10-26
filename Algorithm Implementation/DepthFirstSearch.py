#Depth First search 
def dfs(graph, visit, node):
    visit.append(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visit:
            dfs(graph, visit, neighbor)


graph = {}
n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"Enter node {i+1} name: ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

start = input("Enter starting node: ")

v = []
print("\nDFS Traversal:")
dfs(graph, v, start)
