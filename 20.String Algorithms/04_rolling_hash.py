class RollingHash:
    def __init__(self, s, base=256, mod=10**9 + 7):
        self.s = s
        self.base = base
        self.mod = mod
        self.n = len(s)
        self.prefix = [0] * (self.n + 1)
        self.power = [1] * (self.n + 1)
        for i in range(self.n):
            self.prefix[i + 1] = (self.prefix[i] * base + ord(s[i])) % mod
            self.power[i + 1] = (self.power[i] * base) % mod

    def get_hash(self, l, r):
        return (self.prefix[r + 1] - self.prefix[l] * self.power[r - l + 1]) % self.mod


if __name__ == "__main__":
    rh = RollingHash("hello world")
    print(rh.get_hash(0, 4) == rh.get_hash(6, 10))
