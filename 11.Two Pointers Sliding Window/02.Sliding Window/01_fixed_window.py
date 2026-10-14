def max_sum_fixed(arr, k):
    n = len(arr)
    if n < k:
        return None
    window = sum(arr[:k])
    best = window
    for i in range(k, n):
        window += arr[i] - arr[i - k]
        best = max(best, window)
    return best


if __name__ == "__main__":
    print(max_sum_fixed([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))
