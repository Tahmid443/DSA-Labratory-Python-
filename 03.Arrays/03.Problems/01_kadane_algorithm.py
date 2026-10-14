def kadane(arr):
    max_so_far = curr = arr[0]
    for x in arr[1:]:
        curr = max(x, curr + x)
        max_so_far = max(max_so_far, curr)
    return max_so_far


def kadane_with_indices(arr):
    max_so_far = curr = arr[0]
    start = end = s = 0
    for i in range(1, len(arr)):
        if arr[i] > curr + arr[i]:
            curr = arr[i]
            s = i
        else:
            curr += arr[i]
        if curr > max_so_far:
            max_so_far = curr
            start = s
            end = i
    return max_so_far, start, end


if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(kadane(arr))
    print(kadane_with_indices(arr))
