class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)
        if not self.directed:
            self.graph.setdefault(v, []).append(u)

    def __repr__(self):
        return str(self.graph)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    print(g)
