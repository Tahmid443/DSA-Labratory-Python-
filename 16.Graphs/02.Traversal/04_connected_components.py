def count_components(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        pa, pb = find(a), find(b)
        if pa != pb:
            parent[pa] = pb

    for u, v in edges:
        union(u, v)
    return len(set(find(i) for i in range(n)))


if __name__ == "__main__":
    print(count_components(5, [(0, 1), (2, 3)]))
