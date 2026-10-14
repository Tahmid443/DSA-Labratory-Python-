def first_occurrence(arr, target):
    low, high, res = 0, len(arr) - 1, -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            res = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return res


def last_occurrence(arr, target):
    low, high, res = 0, len(arr) - 1, -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            res = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return res


if __name__ == "__main__":
    arr = [1, 2, 4, 4, 4, 5, 6]
    print(first_occurrence(arr, 4))
    print(last_occurrence(arr, 4))
