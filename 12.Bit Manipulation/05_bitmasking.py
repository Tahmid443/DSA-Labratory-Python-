def subsets_bitmask(nums):
    n = len(nums)
    result = []
    for mask in range(1 << n):
        subset = [nums[i] for i in range(n) if mask & (1 << i)]
        result.append(subset)
    return result


if __name__ == "__main__":
    print(subsets_bitmask([1, 2, 3]))
