def second_largest(arr):
    if len(arr) < 2:
        return None
    first = second = float("-inf")
    for x in arr:
        if x > first:
            second = first
            first = x
        elif x > second and x != first:
            second = x
    return second if second != float("-inf") else None


if __name__ == "__main__":
    print(second_largest([12, 35, 1, 10, 34, 1]))
    print(second_largest([10, 10, 10]))
