from heapq import nsmallest 

# ---------------------------------------------------
# 🚀 Beam Search Algorithm
# ---------------------------------------------------



def beam_search(start, goal, beam_width, graph, heuristic):
    beam = [(start, [start])]   # Initialize beam with the start node
    visited_goal = False

    while beam:
        print(f"Current Beam = {[n for n, _ in beam]}")

        # Goal test
        for node, path in beam:
            if node == goal:
                print(f" Goal found: {node}")
                visited_goal = True
                return path

        # Collect all children of nodes in current beam
        candidates = []
        for node, path in beam:
            children = graph.get(node, [])
            for child in children:
                new_path = path + [child]
                candidates.append((child, new_path))
                print(f"  ➕ New candidate path: {new_path}")

        if not candidates:   # No more nodes to explore
            break

        print(f"Candidates = {[n for n, _ in candidates]}")

        # Select top beam_width nodes with smallest heuristic values
        beam = nsmallest(beam_width, candidates, key=lambda x: heuristic.get(x[0], float("inf")))
        print(f"Selected Top-{beam_width} = {[n for n, _ in beam]}\n")

    if not visited_goal:
        print("❌ Goal not found!")
        return None


# -------------------------------
# 🧩 Main Code (User Input Section)
# -------------------------------
n = int(input("Enter number of nodes: "))
graph = {}
heuristic = {}

print("\n--- Enter Graph Edges ---")
for _ in range(n):
    node = input("Node: ")
    children = input(f"Children of {node} (space separated): ").split()
    graph[node] = children

print("\n--- Enter Heuristic Values ---")
for node in graph:
    h = int(input(f"Heuristic value of {node}: "))
    heuristic[node] = h

start_node = input("\nEnter Start Node: ")
goal_node = input("Enter Goal Node: ")
beam_width = int(input("Enter Beam Width: "))

path = beam_search(start_node, goal_node, beam_width, graph, heuristic)
print("\nFinal Path:", " -> ".join(path) if path else "No path found")
      
