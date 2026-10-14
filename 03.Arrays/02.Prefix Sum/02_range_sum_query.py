class NumArray:
    def __init__(self, nums):
        self.prefix = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + x

    def sum_range(self, i, j):
        return self.prefix[j + 1] - self.prefix[i]


if __name__ == "__main__":
    na = NumArray([-2, 0, 3, -5, 2, -1])
    print(na.sum_range(0, 2))
    print(na.sum_range(2, 5))
    print(na.sum_range(0, 5))
