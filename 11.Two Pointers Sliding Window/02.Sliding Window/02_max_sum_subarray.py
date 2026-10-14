def max_sum_subarray_dynamic(arr):
    """Dynamic window - min length subarray with sum >= target"""
    n = len(arr)
    total = 0
    left = 0
    best = float("inf")
    for right in range(n):
        total += arr[right]
        while total >= 7:
            best = min(best, right - left + 1)
            total -= arr[left]
            left += 1
    return best if best != float("inf") else 0


if __name__ == "__main__":
    print(max_sum_subarray_dynamic([2, 3, 1, 2, 4, 3]))
