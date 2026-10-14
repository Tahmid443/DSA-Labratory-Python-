"""
Compare performance of different complexities
"""

import time
import matplotlib.pyplot as plt


def measure(func, *args):
    start = time.time()
    func(*args)
    return time.time() - start


def o_1(n):
    return 1


def o_log_n(n):
    c = 0
    while n > 1:
        n //= 2
        c += 1
    return c


def o_n(n):
    return sum(range(n))


def o_n_log_n(n):
    c = 0
    for i in range(n):
        j = 1
        while j < n:
            j *= 2
            c += 1
    return c


def o_n_squared(n):
    return sum(i * j for i in range(n) for j in range(n))


if __name__ == "__main__":
    sizes = [10, 50, 100, 500]
    funcs = {
        "O(1)": o_1,
        "O(log n)": o_log_n,
        "O(n)": o_n,
        "O(n log n)": o_n_log_n,
        "O(n^2)": o_n_squared,
    }
    for name, f in funcs.items():
        times = [measure(f, n) for n in sizes]
        print(f"{name}: {[f'{t:.6f}' for t in times]}")
