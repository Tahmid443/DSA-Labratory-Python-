def factorial(n):
    if n < 0:
        raise ValueError("Negative not allowed")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def factorial_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print(factorial(5))
    print(factorial_iter(5))
