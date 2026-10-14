def insert_at(arr, index, value):
    if index < 0 or index > len(arr):
        raise IndexError("Invalid index")
    arr.append(None)
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]
    arr[index] = value
    return arr


def insert_end(arr, value):
    arr.append(value)
    return arr


def insert_beginning(arr, value):
    arr.insert(0, value)
    return arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print(insert_at(arr, 2, 99))
    print(insert_end(arr, 100))
    print(insert_beginning(arr, 0))
