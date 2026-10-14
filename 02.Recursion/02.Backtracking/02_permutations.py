def permutations(nums):
    result = []

    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return
        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i + 1 :])
            path.pop()

    backtrack([], nums)
    return result


def permutations_swap(nums):
    result = []
    nums = nums[:]

    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return result


if __name__ == "__main__":
    print(permutations([1, 2, 3]))
    print(permutations_swap([1, 2, 3]))
