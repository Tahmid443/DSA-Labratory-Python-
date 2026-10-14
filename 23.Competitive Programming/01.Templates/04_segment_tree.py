class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self._build(arr, 0, 0, self.n - 1)

    def _build(self, arr, node, l, r):
        if l == r:
            self.tree[node] = arr[l]
            return
        mid = (l + r) // 2
        self._build(arr, 2 * node + 1, l, mid)
        self._build(arr, 2 * node + 2, mid + 1, r)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, l, r):
        return self._query(0, 0, self.n - 1, l, r)

    def _query(self, node, l, r, ql, qr):
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2
        return self._query(2 * node + 1, l, mid, ql, qr) + self._query(
            2 * node + 2, mid + 1, r, ql, qr
        )


if __name__ == "__main__":
    st = SegmentTree([1, 2, 3, 4, 5])
    print(st.query(1, 3))
