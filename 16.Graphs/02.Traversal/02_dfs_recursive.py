def dfs(graph, node, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []
    visited.add(node)
    order.append(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)
    return order


if __name__ == "__main__":
    g = {0: [1, 2], 1: [3], 2: [3], 3: []}
    print(dfs(g, 0))
