def is_bit_set(n, i):
    return (n >> i) & 1 == 1


def is_bit_set_mask(n, i):
    return n & (1 << i) != 0


if __name__ == "__main__":
    print(is_bit_set(5, 0))  # True
    print(is_bit_set(5, 1))  # False
    print(is_bit_set_mask(5, 2))  # True
