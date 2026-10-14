class DifferenceArray:
    """Range update in O(1), point query in O(n)"""

    def __init__(self, n):
        self.diff = [0] * (n + 1)

    def update(self, l, r, val):
        self.diff[l] += val
        if r + 1 < len(self.diff):
            self.diff[r + 1] -= val

    def get_array(self, n):
        result = [0] * n
        result[0] = self.diff[0]
        for i in range(1, n):
            result[i] = result[i - 1] + self.diff[i]
        return result


if __name__ == "__main__":
    da = DifferenceArray(5)
    da.update(1, 3, 10)
    da.update(2, 4, 5)
    print(da.get_array(5))
