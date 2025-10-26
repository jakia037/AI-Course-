# ------------------------------------
# 🎮 Minimax Algorithm Implementation (Python)
# ------------------------------------

def minimax(tree, node, is_maximizing):
    # Base case — leaf node
    if isinstance(tree[node], int):
        return tree[node]

    # Maximizing player
    if is_maximizing:
        best = -float('inf')
        for child in tree[node]:
            val = minimax(tree, child, False)
            best = max(best, val)
        return best

    # Minimizing player
    else:
        best = float('inf')
        for child in tree[node]:
            val = minimax(tree, child, True)
            best = min(best, val)
        return best


# ---------------------------------------
# 🧩 User Input Section
# ---------------------------------------
values = list(map(int, input("Enter leaf node values separated by space: ").split()))
n = len(values)

tree = {}

def build_tree(name, vals):
    if len(vals) == 1:
        tree[name] = vals[0]
    else:
        left = name + "L"
        right = name + "R"
        tree[name] = [left, right]
        mid = len(vals) // 2
        build_tree(left, vals[:mid])
        build_tree(right, vals[mid:])

# Build tree & run algorithm
build_tree("root", values)

result = minimax(tree, "root", True)
print("Optimal value for maximizing player:", result)
      
