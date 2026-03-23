# Depth First Search - Full Program

# Recursive DFS
def dfs_recursive(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph.get(node, []):
            dfs_recursive(graph, neighbor, visited)


# Iterative DFS using stack
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            # Add neighbors in reverse order for correct traversal
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)


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

    print("DFS Recursive:")
    visited_set = set()
    dfs_recursive(graph, start_node, visited_set)

    print("\nDFS Iterative:")
    dfs_iterative(graph, start_node)