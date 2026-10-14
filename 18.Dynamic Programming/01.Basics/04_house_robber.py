def rob(nums):
    prev = curr = 0
    for x in nums:
        prev, curr = curr, max(curr, prev + x)
    return curr


def rob_circular(nums):
    if len(nums) == 1:
        return nums[0]

    def helper(arr):
        prev = curr = 0
        for x in arr:
            prev, curr = curr, max(curr, prev + x)
        return curr

    return max(helper(nums[:-1]), helper(nums[1:]))


if __name__ == "__main__":
    print(rob([2, 7, 9, 3, 1]))
    print(rob_circular([2, 3, 2]))
