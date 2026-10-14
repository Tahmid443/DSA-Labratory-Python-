def reverse_two_pointer(arr):
    i, j = 0, len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr


def reverse_slice(arr):
    return arr[::-1]


def reverse_recursive(arr, i=0):
    if i >= len(arr) // 2:
        return arr
    arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]
    return reverse_recursive(arr, i + 1)


if __name__ == "__main__":
    print(reverse_two_pointer([1, 2, 3, 4, 5]))
    print(reverse_slice([1, 2, 3, 4, 5]))
    print(reverse_recursive([1, 2, 3, 4, 5]))
