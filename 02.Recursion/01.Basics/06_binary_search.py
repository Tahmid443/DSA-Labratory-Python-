def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    return binary_search(arr, target, low, mid - 1)


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13]
    print(binary_search(arr, 7))
    print(binary_search(arr, 6))
