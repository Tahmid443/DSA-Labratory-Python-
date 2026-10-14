import heapq


def kth_largest(nums, k):
    min_heap = []
    for x in nums:
        heapq.heappush(min_heap, x)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]


if __name__ == "__main__":
    print(kth_largest([3, 2, 1, 5, 6, 4], 2))
