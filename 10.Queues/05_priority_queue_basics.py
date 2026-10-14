import heapq


class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.counter = 0

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, self.counter, item))
        self.counter += 1

    def pop(self):
        if not self.heap:
            raise IndexError("Empty")
        return heapq.heappop(self.heap)[2]


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push("task1", 3)
    pq.push("task2", 1)
    pq.push("task3", 2)
    print(pq.pop(), pq.pop(), pq.pop())
