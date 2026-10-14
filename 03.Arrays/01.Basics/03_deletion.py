def delete_at(arr, index):
    if index < 0 or index >= len(arr):
        raise IndexError("Invalid index")
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]
    arr.pop()
    return arr


def delete_value(arr, value):
    if value in arr:
        arr.remove(value)
    return arr


def delete_all_occurrences(arr, value):
    return [x for x in arr if x != value]


if __name__ == "__main__":
    print(delete_at([1, 2, 3, 4, 5], 2))
    print(delete_value([1, 2, 3, 2, 4], 2))
    print(delete_all_occurrences([1, 2, 3, 2, 4], 2))
