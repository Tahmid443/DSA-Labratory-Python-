class HashSet:
    def __init__(self, size=16):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def add(self, key):
        idx = self._hash(key)
        if key not in self.buckets[idx]:
            self.buckets[idx].append(key)

    def contains(self, key):
        return key in self.buckets[self._hash(key)]

    def remove(self, key):
        idx = self._hash(key)
        if key in self.buckets[idx]:
            self.buckets[idx].remove(key)


if __name__ == "__main__":
    hs = HashSet()
    hs.add(1)
    hs.add(2)
    hs.add(1)
    print(hs.contains(1), hs.contains(3))
    hs.remove(1)
    print(hs.contains(1))
