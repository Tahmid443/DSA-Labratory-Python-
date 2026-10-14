from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        if not self.items:
            raise IndexError("Queue is empty")
        return self.items.popleft()

    def front(self):
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue(), q.front())
