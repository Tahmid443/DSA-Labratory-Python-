"""
Recursive function complexity analysis
"""

from functools import lru_cache


# T(n) = T(n-1) + O(1) => O(n)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# T(n) = T(n-1) + T(n-2) => O(2^n) without memo, O(n) with
@lru_cache(maxsize=None)
def fibonacci_memo(n):
    if n <= 1:
        return n
    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)


def fibonacci_naive(n):
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


# T(n) = 2T(n/2) + O(n) => O(n log n)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(l, r):
    res, i, j = [], 0, 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
    res.extend(l[i:])
    res.extend(r[j:])
    return res


if __name__ == "__main__":
    print(f"Factorial(5): {factorial(5)}")
    print(f"Fib memo(30): {fibonacci_memo(30)}")
    print(f"Fib naive(10): {fibonacci_naive(10)}")
    print(f"Merge sort: {merge_sort([5,2,8,1,9,3])}")
