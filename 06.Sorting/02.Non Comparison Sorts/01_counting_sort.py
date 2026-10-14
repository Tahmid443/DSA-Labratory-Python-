def counting_sort(arr):
    if not arr:
        return arr
    mn, mx = min(arr), max(arr)
    count = [0] * (mx - mn + 1)
    for x in arr:
        count[x - mn] += 1
    result = []
    for i, c in enumerate(count):
        result.extend([i + mn] * c)
    return result


if __name__ == "__main__":
    print(counting_sort([4, 2, 2, 8, 3, 3, 1]))
