def bellman_ford(n, edges, start):
    dist = [float("inf")] * n
    dist[start] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for u, v, w in edges:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            return None  # negative cycle
    return dist


if __name__ == "__main__":
    edges = [(0, 1, 4), (0, 2, 5), (1, 2, -3), (2, 3, 2)]
    print(bellman_ford(4, edges, 0))
