# Iterative Deepening Depth-First Search (IDDFS)

# Depth-Limited Search (DLS)
def dls(graph, node, goal, depth, visited):
    if depth == 0:
        return node == goal

    if depth > 0:
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dls(graph, neighbor, goal, depth - 1, visited):
                    return True
        visited.remove(node)  # backtrack

    return False


# IDDFS function
def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"Searching at depth: {depth}")
        visited = set()

        if dls(graph, start, goal, depth, visited):
            return True

    return False


# Main program
if __name__ == "__main__":
    # Example graph (Adjacency List)
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    start_node = 'A'
    goal_node = 'F'
    max_depth = 3

    found = iddfs(graph, start_node, goal_node, max_depth)

    if found:
        print("Goal Found!")
    else:
        print("Goal Not Found.")