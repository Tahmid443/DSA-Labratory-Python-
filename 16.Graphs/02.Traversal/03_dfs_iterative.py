def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    order = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            stack.extend(graph.get(node, []))
    return order


if __name__ == "__main__":
    g = {0: [1, 2], 1: [3], 2: [3], 3: []}
    print(dfs_iterative(g, 0))
