def compress(arr):
    sorted_unique = sorted(set(arr))
    mapping = {v: i for i, v in enumerate(sorted_unique)}
    return [mapping[x] for x in arr], mapping


if __name__ == "__main__":
    arr = [100, 5, 200, 5, 100]
    print(compress(arr))
