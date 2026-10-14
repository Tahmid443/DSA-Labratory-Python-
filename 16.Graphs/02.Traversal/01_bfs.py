from collections import deque


def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


if __name__ == "__main__":
    g = {0: [1, 2], 1: [3], 2: [3], 3: []}
    print(bfs(g, 0))
