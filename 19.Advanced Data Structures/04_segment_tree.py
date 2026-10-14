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

    def query(self, ql, qr):
        return self._query(0, 0, self.n - 1, ql, qr)

    def _query(self, node, l, r, ql, qr):
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2
        return self._query(2 * node + 1, l, mid, ql, qr) + self._query(
            2 * node + 2, mid + 1, r, ql, qr
        )

    def update(self, idx, val):
        self._update(0, 0, self.n - 1, idx, val)

    def _update(self, node, l, r, idx, val):
        if l == r:
            self.tree[node] = val
            return
        mid = (l + r) // 2
        if idx <= mid:
            self._update(2 * node + 1, l, mid, idx, val)
        else:
            self._update(2 * node + 2, mid + 1, r, idx, val)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]


if __name__ == "__main__":
    st = SegmentTree([1, 3, 5, 7, 9, 11])
    print(st.query(1, 3))
    st.update(1, 10)
    print(st.query(1, 3))
