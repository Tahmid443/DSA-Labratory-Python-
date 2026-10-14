from collections import deque


class MaxFlow:
    def __init__(self, n):
        self.n = n
        self.capacity = [[0] * n for _ in range(n)]
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, cap):
        self.capacity[u][v] += cap
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs(self, s, t, parent):
        visited = [False] * self.n
        visited[s] = True
        q = deque([s])
        while q:
            u = q.popleft()
            for v in self.adj[u]:
                if not visited[v] and self.capacity[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    q.append(v)
        return visited[t]

    def max_flow(self, s, t):
        parent = [-1] * self.n
        flow = 0
        while self.bfs(s, t, parent):
            path_flow = float("inf")
            v = t
            while v != s:
                u = parent[v]
                path_flow = min(path_flow, self.capacity[u][v])
                v = u
            v = t
            while v != s:
                u = parent[v]
                self.capacity[u][v] -= path_flow
                self.capacity[v][u] += path_flow
                v = u
            flow += path_flow
        return flow


if __name__ == "__main__":
    mf = MaxFlow(6)
    mf.add_edge(0, 1, 16)
    mf.add_edge(0, 2, 13)
    mf.add_edge(1, 2, 10)
    mf.add_edge(2, 1, 4)
    mf.add_edge(1, 3, 12)
    mf.add_edge(3, 2, 9)
    mf.add_edge(2, 4, 14)
    mf.add_edge(4, 3, 7)
    mf.add_edge(3, 5, 20)
    mf.add_edge(4, 5, 4)
    print(mf.max_flow(0, 5))
