def binary_search_rec(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search_rec(arr, target, mid + 1, high)
    return binary_search_rec(arr, target, low, mid - 1)


if __name__ == "__main__":
    print(binary_search_rec([1, 3, 5, 7, 9, 11], 9))
