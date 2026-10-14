"""
Nested loops and their complexity
"""


def nested_loops_n_squared(n):
    """O(n^2)"""
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count


def nested_loops_triangular(n):
    """O(n^2) but half iterations"""
    count = 0
    for i in range(n):
        for j in range(i, n):
            count += 1
    return count


def nested_loops_n_cubed(n):
    """O(n^3)"""
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                count += 1
    return count


def log_nested(n):
    """O(n log n)"""
    count = 0
    for i in range(n):
        j = 1
        while j < n:
            count += 1
            j *= 2
    return count


if __name__ == "__main__":
    print(f"O(n^2) n=5: {nested_loops_n_squared(5)}")
    print(f"Triangular n=5: {nested_loops_triangular(5)}")
    print(f"O(n^3) n=3: {nested_loops_n_cubed(3)}")
    print(f"O(n log n) n=8: {log_nested(8)}")
