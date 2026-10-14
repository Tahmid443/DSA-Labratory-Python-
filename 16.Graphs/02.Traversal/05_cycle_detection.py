def has_cycle_undirected(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v in edges:
        pu, pv = find(u), find(v)
        if pu == pv:
            return True
        parent[pu] = pv
    return False


def has_cycle_directed(n, edges):
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n

    def dfs(u):
        color[u] = GRAY
        for v in graph[u]:
            if color[v] == GRAY:
                return True
            if color[v] == WHITE and dfs(v):
                return True
        color[u] = BLACK
        return False

    return any(color[i] == WHITE and dfs(i) for i in range(n))


if __name__ == "__main__":
    print(has_cycle_undirected(4, [(0, 1), (1, 2), (2, 0)]))
    print(has_cycle_directed(4, [(0, 1), (1, 2), (2, 0)]))
