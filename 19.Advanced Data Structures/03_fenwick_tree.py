class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        i += 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        """Prefix sum [0..i]"""
        i += 1
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total

    def range_sum(self, l, r):
        return self.query(r) - (self.query(l - 1) if l > 0 else 0)


if __name__ == "__main__":
    ft = FenwickTree(5)
    for i, v in enumerate([1, 2, 3, 4, 5]):
        ft.update(i, v)
    print(ft.query(4))
    print(ft.range_sum(1, 3))
