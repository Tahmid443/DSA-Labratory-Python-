def reverse_string(s):
    return s[::-1]


def reverse_inplace(s):
    arr = list(s)
    i, j = 0, len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return "".join(arr)


if __name__ == "__main__":
    print(reverse_string("hello"))
    print(reverse_inplace("world"))
