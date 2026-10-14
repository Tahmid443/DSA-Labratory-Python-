def can_jump(nums):
    max_reach = 0
    for i, x in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + x)
    return True


def min_jumps(nums):
    jumps = 0
    curr_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == curr_end:
            jumps += 1
            curr_end = farthest
    return jumps


if __name__ == "__main__":
    print(can_jump([2, 3, 1, 1, 4]))
    print(min_jumps([2, 3, 1, 1, 4]))
