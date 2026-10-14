def pair_sum_sorted(arr, target):
    i, j = 0, len(arr) - 1
    while i < j:
        s = arr[i] + arr[j]
        if s == target:
            return (i, j)
        elif s < target:
            i += 1
        else:
            j -= 1
    return None


if __name__ == "__main__":
    print(pair_sum_sorted([1, 2, 3, 4, 6], 6))
