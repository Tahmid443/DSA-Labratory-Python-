from collections import deque


def bfs(graph, start):
    visited = [False] * len(graph)
    dist = [-1] * len(graph)
    visited[start] = True
    dist[start] = 0
    q = deque([start])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


if __name__ == "__main__":
    g = [[1, 2], [0, 3], [0, 3], [1, 2]]
    print(bfs(g, 0))
