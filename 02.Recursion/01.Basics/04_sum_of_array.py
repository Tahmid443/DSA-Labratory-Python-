def sum_array(arr):
    if not arr:
        return 0
    return arr[0] + sum_array(arr[1:])


def sum_array_index(arr, i=0):
    if i == len(arr):
        return 0
    return arr[i] + sum_array_index(arr, i + 1)


if __name__ == "__main__":
    print(sum_array([1, 2, 3, 4, 5]))
    print(sum_array_index([1, 2, 3, 4, 5]))
