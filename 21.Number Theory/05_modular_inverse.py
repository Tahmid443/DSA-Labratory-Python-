def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def mod_inverse(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError("Inverse doesn't exist")
    return x % m


def fermat_inverse(a, p):
    return pow(a, p - 2, p)


if __name__ == "__main__":
    print(mod_inverse(3, 11))
    print(fermat_inverse(3, 11))
