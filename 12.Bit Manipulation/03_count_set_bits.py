def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def count_set_bits_brian(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


def count_set_bits_builtin(n):
    return bin(n).count("1")


if __name__ == "__main__":
    print(count_set_bits(13))
    print(count_set_bits_brian(13))
    print(count_set_bits_builtin(13))
