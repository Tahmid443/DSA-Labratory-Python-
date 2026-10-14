def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def gcd_rec(a, b):
    return a if b == 0 else gcd_rec(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


if __name__ == "__main__":
    print(gcd(48, 18))
    print(lcm(4, 6))
