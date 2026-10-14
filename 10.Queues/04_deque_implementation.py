class Deque:
    def __init__(self):
        self.items = []

    def append_left(self, x):
        self.items.insert(0, x)

    def append_right(self, x):
        self.items.append(x)

    def pop_left(self):
        if not self.items:
            raise IndexError("Deque empty")
        return self.items.pop(0)

    def pop_right(self):
        if not self.items:
            raise IndexError("Deque empty")
        return self.items.pop()


if __name__ == "__main__":
    d = Deque()
    d.append_right(1)
    d.append_left(0)
    d.append_right(2)
    print(d.pop_left(), d.pop_right())
