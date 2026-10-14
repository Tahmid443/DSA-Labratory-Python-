def single_number(nums):
    result = 0
    for x in nums:
        result ^= x
    return result


def find_two_singles(nums):
    xor_all = 0
    for x in nums:
        xor_all ^= x
    lowbit = xor_all & -xor_all
    a = b = 0
    for x in nums:
        if x & lowbit:
            a ^= x
        else:
            b ^= x
    return a, b


if __name__ == "__main__":
    print(single_number([4, 1, 2, 1, 2]))
    print(find_two_singles([1, 2, 1, 3, 2, 5]))
