def longest_consecutive(nums):
    s = set(nums)
    best = 0
    for x in s:
        if x - 1 not in s:
            y = x
            while y + 1 in s:
                y += 1
            best = max(best, y - x + 1)
    return best


if __name__ == "__main__":
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))
