def find_min_max(arr):
    if not arr:
        return None, None
    mn = mx = arr[0]
    for x in arr[1:]:
        if x < mn:
            mn = x
        if x > mx:
            mx = x
    return mn, mx


def find_min_max_tournament(arr):
    n = len(arr)
    if n % 2 == 0:
        mn = min(arr[0], arr[1])
        mx = max(arr[0], arr[1])
        start = 2
    else:
        mn = mx = arr[0]
        start = 1
    for i in range(start, n - 1, 2):
        if arr[i] < arr[i + 1]:
            mn = min(mn, arr[i])
            mx = max(mx, arr[i + 1])
        else:
            mn = min(mn, arr[i + 1])
            mx = max(mx, arr[i])
    return mn, mx


if __name__ == "__main__":
    print(find_min_max([3, 1, 4, 1, 5, 9, 2, 6]))
    print(find_min_max_tournament([3, 1, 4, 1, 5, 9, 2, 6]))
