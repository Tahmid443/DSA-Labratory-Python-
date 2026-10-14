from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_manual_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_manual_memo(n - 1, memo) + fib_manual_memo(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    print(fib(40))
    print(fib_manual_memo(40))
