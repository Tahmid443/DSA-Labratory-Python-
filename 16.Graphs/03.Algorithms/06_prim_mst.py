import heapq


def prim(graph, start=0):
    visited = set([start])
    edges = [(w, start, v) for v, w in graph[start]]
    heapq.heapify(edges)
    mst = []
    while edges:
        w, u, v = heapq.heappop(edges)
        if v in visited:
            continue
        visited.add(v)
        mst.append((u, v, w))
        for nxt, wt in graph[v]:
            if nxt not in visited:
                heapq.heappush(edges, (wt, v, nxt))
    return mst


if __name__ == "__main__":
    g = {
        0: [(1, 10), (2, 6), (3, 5)],
        1: [(0, 10), (3, 15)],
        2: [(0, 6), (3, 4)],
        3: [(0, 5), (1, 15), (2, 4)],
    }
    print(prim(g))
