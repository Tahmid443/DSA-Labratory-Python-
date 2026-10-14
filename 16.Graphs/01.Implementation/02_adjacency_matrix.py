class GraphMatrix:
    def __init__(self, n):
        self.n = n
        self.matrix = [[0] * n for _ in range(n)]

    def add_edge(self, u, v, w=1):
        self.matrix[u][v] = w
        self.matrix[v][u] = w

    def __repr__(self):
        return "\n".join(str(row) for row in self.matrix)


if __name__ == "__main__":
    g = GraphMatrix(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    print(g)
