class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def enqueue(self, x):
        if (self.rear + 1) % self.capacity == self.front:
            raise OverflowError("Queue full")
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = x

    def dequeue(self):
        if self.front == -1:
            raise IndexError("Queue empty")
        val = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return val


if __name__ == "__main__":
    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    print(cq.dequeue())
