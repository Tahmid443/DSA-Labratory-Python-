def subset_sums(arr):
    sums = [0]
    for x in arr:
        sums += [s + x for s in sums]
    return sums


def meet_in_middle(arr, target):
    mid = len(arr) // 2
    left = subset_sums(arr[:mid])
    right = subset_sums(arr[mid:])
    right.sort()
    import bisect

    count = 0
    for s in left:
        need = target - s
        count += bisect.bisect_right(right, need) - bisect.bisect_left(right, need)
    return count


if __name__ == "__main__":
    print(meet_in_middle([1, 2, 3, 4, 5], 5))
