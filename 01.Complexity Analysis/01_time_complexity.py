"""
Time Complexity Examples - Big-O Notation
O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n) < O(n!)
"""
import time

# O(1) - Constant Time
def constant_time(arr):
    return arr[0] if arr else None

# O(log n) - Logarithmic
def logarithmic_time(n):
    count = 0
    while n > 1:
        n //= 2
        count += 1
    return count

# O(n) - Linear
def linear_time(arr):
    total = 0
    for x in arr:
        total += x
    return total

# O(n log n) - Linearithmic (merge sort)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:]); result.extend(right[j:])
    return result

# O(n^2) - Quadratic
def quadratic_time(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count

# O(2^n) - Exponential
def exponential_time(n):
    if n <= 1:
        return n
    return exponential_time(n - 1) + exponential_time(n - 2)

# O(n!) - Factorial
def permutations_count(n):
    if n <= 1:
        return 1
    return n * permutations_count(n - 1)

if __name__ == "__main__":
    arr = list(range(1000))
    print(f"Constant: {constant_time(arr)}")
    print(f"Logarithmic(1024): {logarithmic_time(1024)}")
    print(f"Linear sum: {linear_time(arr)}")
    print(f"Merge sorted: {merge_sort([3,1,4,1,5,9,2,6])}")
    print(f"Quadratic(100): {quadratic_time(list(range(100)))}")
    print(f"Exponential(10): {exponential_time(10)}")
    print(f"Factorial(5): {permutations_count(5)}")