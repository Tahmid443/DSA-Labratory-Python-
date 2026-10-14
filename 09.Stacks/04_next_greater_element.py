def next_greater(arr):
    n = len(arr)
    result = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result


if __name__ == "__main__":
    print(next_greater([4, 5, 2, 10, 8]))
