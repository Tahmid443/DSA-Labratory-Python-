from collections import Counter


def frequency_counter(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    return freq


def top_k_frequent(arr, k):
    return [x for x, _ in Counter(arr).most_common(k)]


if __name__ == "__main__":
    print(frequency_counter([1, 2, 2, 3, 3, 3]))
    print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
