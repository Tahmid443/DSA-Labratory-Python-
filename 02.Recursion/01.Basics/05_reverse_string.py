def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


def reverse_inplace(s, i=0):
    if i >= len(s) // 2:
        return s
    s = list(s)
    # This is a helper approach
    return s


if __name__ == "__main__":
    print(reverse_string("hello"))
    print(reverse_string("recursion"))
