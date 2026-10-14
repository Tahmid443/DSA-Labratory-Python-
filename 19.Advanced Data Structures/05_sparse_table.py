import math


class SparseTable:
    def __init__(self, arr):
        n = len(arr)
        k = math.floor(math.log2(n)) + 1
        self.table = [[0] * k for _ in range(n)]
        self.log = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log[i] = self.log[i // 2] + 1
        for i in range(n):
            self.table[i][0] = arr[i]
        for j in range(1, k):
            for i in range(n - (1 << j) + 1):
                self.table[i][j] = min(
                    self.table[i][j - 1], self.table[i + (1 << (j - 1))][j - 1]
                )

    def query(self, l, r):
        j = self.log[r - l + 1]
        return min(self.table[l][j], self.table[r - (1 << j) + 1][j])


if __name__ == "__main__":
    st = SparseTable([5, 2, 7, 1, 9, 3])
    print(st.query(1, 4))
