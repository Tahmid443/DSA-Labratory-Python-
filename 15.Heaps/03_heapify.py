def heapify(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        _sift_down(arr, n, i)
    return arr


def _sift_down(arr, n, i):
    while True:
        smallest = i
        l, r = 2 * i + 1, 2 * i + 2
        if l < n and arr[l] < arr[smallest]:
            smallest = l
        if r < n and arr[r] < arr[smallest]:
            smallest = r
        if smallest == i:
            break
        arr[i], arr[smallest] = arr[smallest], arr[i]
        i = smallest


if __name__ == "__main__":
    print(heapify([3, 1, 6, 5, 2, 4]))
