def max_area(height):
    i, j = 0, len(height) - 1
    best = 0
    while i < j:
        h = min(height[i], height[j])
        best = max(best, h * (j - i))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return best


if __name__ == "__main__":
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
