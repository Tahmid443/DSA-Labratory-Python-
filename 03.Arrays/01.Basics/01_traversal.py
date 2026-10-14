def traverse(arr):
    for i in range(len(arr)):
        print(f"Index {i}: {arr[i]}")


def traverse_foreach(arr):
    for val in arr:
        print(val)


def traverse_enumerate(arr):
    for i, val in enumerate(arr):
        print(f"{i}: {val}")


if __name__ == "__main__":
    traverse([10, 20, 30, 40])
