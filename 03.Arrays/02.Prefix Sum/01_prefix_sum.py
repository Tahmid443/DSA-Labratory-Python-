def build_prefix_sum(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix


def range_sum(prefix, l, r):
    """Sum of arr[l..r] inclusive"""
    return prefix[r + 1] - prefix[l]


if __name__ == "__main__":
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    prefix = build_prefix_sum(arr)
    print(prefix)
    print(range_sum(prefix, 2, 5))
