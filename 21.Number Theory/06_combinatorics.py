def ncr(n, r):
    if r > n:
        return 0
    r = min(r, n - r)
    result = 1
    for i in range(r):
        result = result * (n - i) // (i + 1)
    return result


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def npr(n, r):
    return factorial(n) // factorial(n - r)


if __name__ == "__main__":
    print(ncr(5, 2))
    print(npr(5, 2))
