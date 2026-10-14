def lis(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def lis_binary(nums):
    import bisect

    tails = []
    for x in nums:
        idx = bisect.bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            tails[idx] = x
    return len(tails)


if __name__ == "__main__":
    print(lis([10, 9, 2, 5, 3, 7, 101, 18]))
    print(lis_binary([10, 9, 2, 5, 3, 7, 101, 18]))
