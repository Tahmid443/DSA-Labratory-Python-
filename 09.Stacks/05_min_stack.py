class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]


if __name__ == "__main__":
    ms = MinStack()
    ms.push(3)
    ms.push(5)
    ms.push(2)
    ms.push(1)
    print(ms.get_min())
    ms.pop()
    print(ms.get_min())
