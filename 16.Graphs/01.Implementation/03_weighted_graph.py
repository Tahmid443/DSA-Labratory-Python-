class WeightedGraph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_edge(self, u, v, w):
        self.graph.setdefault(u, []).append((v, w))
        if not self.directed:
            self.graph.setdefault(v, []).append((u, w))

    def __repr__(self):
        return str(self.graph)


if __name__ == "__main__":
    g = WeightedGraph()
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 1)
    g.add_edge(1, 2, 2)
    print(g)
