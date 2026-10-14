def max_subarray_divide(arr):
    def helper(l, r):
        if l == r:
            return arr[l]
        mid = (l + r) // 2
        left = helper(l, mid)
        right = helper(mid + 1, r)
        # cross
        left_sum = float("-inf")
        s = 0
        for i in range(mid, l - 1, -1):
            s += arr[i]
            left_sum = max(left_sum, s)
        right_sum = float("-inf")
        s = 0
        for i in range(mid + 1, r + 1):
            s += arr[i]
            right_sum = max(right_sum, s)
        return max(left, right, left_sum + right_sum)

    return helper(0, len(arr) - 1)


def kadane(arr):
    max_so_far = curr = arr[0]
    for x in arr[1:]:
        curr = max(x, curr + x)
        max_so_far = max(max_so_far, curr)
    return max_so_far


if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_subarray_divide(arr))
    print(kadane(arr))
