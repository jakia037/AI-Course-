def alphabeta(node_index, depth, values, alpha, beta, is_maximizing, pruned_nodes):
    # Base condition: leaf node or depth limit reached
    if depth == 0 or node_index >= len(values):
        return values[node_index]
    
    if is_maximizing:
        best = float("-inf")
        for i in range(2):  # binary tree (2 children)
            child_index = node_index * 2 + i + 1
            if child_index < len(values):
                val = alphabeta(child_index, depth - 1, values, alpha, beta, False, pruned_nodes)
                best = max(best, val)
                alpha = max(alpha, best)
                if beta <= alpha:
                    # prune remaining child nodes
                    left_over = []
                    for j in range(i + 1, 2):
                        ci = node_index * 2 + j + 1
                        if ci < len(values):
                            left_over.append(ci)
                    if left_over:
                        pruned_nodes.extend(left_over)
                    break
        return best
    
    else:  # Minimizing player
        best = float("inf")
        for i in range(2):
            child_index = node_index * 2 + i + 1
            if child_index < len(values):
                val = alphabeta(child_index, depth - 1, values, alpha, beta, True, pruned_nodes)
                best = min(best, val)
                beta = min(beta, best)
                if beta <= alpha:
                    # prune remaining child nodes
                    left_over = []
                    for j in range(i + 1, 2):
                        ci = node_index * 2 + j + 1
                        if ci < len(values):
                            left_over.append(ci)
                    if left_over:
                        pruned_nodes.extend(left_over)
                    break
        return best


# -----------------------------
# 🔹 Input Section
# -----------------------------
n = int(input("Enter total number of leaf nodes: "))
values = []
print("Enter leaf node values:")
for i in range(n):
    values.append(int(input(f"Value[{i}]: ")))

depth = int(input("Enter depth of tree: "))
first_player = input("Enter who starts first (max/min): ").strip().lower()
is_maximizing = True if first_player == "max" else False

# -----------------------------
# 🔹 Run Alpha-Beta Algorithm
# -----------------------------
pruned_nodes = []
optimal_value = alphabeta(0, depth, values, float("-inf"), float("inf"), is_maximizing, pruned_nodes)

# -----------------------------
# 🔹 Output Section
# -----------------------------
print("\n===== RESULT =====")
print("Optimal Value (Best Outcome):", optimal_value)
print("Total Pruned Nodes:", len(pruned_nodes))
print("Pruned Node Indexes:", pruned_nodes)
if pruned_nodes:
    print("Maximum Pruned Node Index:", max(pruned_nodes))
                                
