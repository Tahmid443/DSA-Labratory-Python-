def linear_search(arr, target):
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1


def linear_search_all(arr, target):
    return [i for i, x in enumerate(arr) if x == target]


if __name__ == "__main__":
    print(linear_search([4, 2, 7, 1, 9], 7))
    print(linear_search_all([1, 2, 1, 3, 1], 1))
