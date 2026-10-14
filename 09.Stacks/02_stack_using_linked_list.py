class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, x):
        new = Node(x)
        new.next = self.top
        self.top = new
        self._size += 1

    def pop(self):
        if not self.top:
            raise IndexError("Stack is empty")
        val = self.top.data
        self.top = self.top.next
        self._size -= 1
        return val

    def peek(self):
        if not self.top:
            raise IndexError("Stack is empty")
        return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    print(s.pop(), s.peek())
