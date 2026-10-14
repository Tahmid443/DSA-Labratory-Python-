def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def first_true(lo, hi, pred):
    """Find first x in [lo, hi] where pred(x) is True"""
    while lo < hi:
        mid = (lo + hi) // 2
        if pred(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


if __name__ == "__main__":
    print(binary_search([1, 3, 5, 7, 9], 5))
    print(first_true(1, 100, lambda x: x * x >= 50))
