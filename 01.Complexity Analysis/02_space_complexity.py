"""
Space Complexity Examples
"""
# O(1) space
def sum_array(arr):
    total = 0
    for x in arr:
        total += x
    return total

# O(n) space - creating a new list
def double_array(arr):
    return [x * 2 for x in arr]

# O(n) space - recursion stack
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# O(n^2) space - 2D matrix
def create_matrix(n):
    return [[0] * n for _ in range(n)]

# O(log n) space - recursive binary search
def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

if __name__ == "__main__":
    print(sum_array([1, 2, 3, 4]))
    print(double_array([1, 2, 3]))
    print(factorial(5))
    print(binary_search([1, 2, 3, 4, 5], 4))