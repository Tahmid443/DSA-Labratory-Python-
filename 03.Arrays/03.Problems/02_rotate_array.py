def rotate_right(arr, k):
    n = len(arr)
    k %= n
    return arr[-k:] + arr[:-k] if k else arr


def rotate_right_inplace(arr, k):
    n = len(arr)
    k %= n

    def reverse(l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
    return arr


if __name__ == "__main__":
    print(rotate_right([1, 2, 3, 4, 5, 6, 7], 3))
    print(rotate_right_inplace([1, 2, 3, 4, 5, 6, 7], 3))
