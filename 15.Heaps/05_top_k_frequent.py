import heapq
from collections import Counter


def top_k_frequent(nums, k):
    count = Counter(nums)
    return [x for x, _ in heapq.nlargest(k, count.items(), key=lambda p: p[1])]


if __name__ == "__main__":
    print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
