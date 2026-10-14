def bucket_sort(arr):
    if not arr:
        return arr
    n = len(arr)
    mn, mx = min(arr), max(arr)
    if mn == mx:
        return arr
    buckets = [[] for _ in range(n)]
    for x in arr:
        idx = int((x - mn) / (mx - mn) * (n - 1))
        buckets[idx].append(x)
    result = []
    for b in buckets:
        result.extend(sorted(b))
    return result


if __name__ == "__main__":
    print(bucket_sort([0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]))
