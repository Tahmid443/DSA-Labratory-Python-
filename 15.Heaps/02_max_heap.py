class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            raise IndexError("Empty")
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root

    def _sift_up(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2

    def _sift_down(self, i):
        n = len(self.heap)
        while True:
            largest = i
            l, r = 2 * i + 1, 2 * i + 2
            if l < n and self.heap[l] > self.heap[largest]:
                largest = l
            if r < n and self.heap[r] > self.heap[largest]:
                largest = r
            if largest == i:
                break
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest


if __name__ == "__main__":
    h = MaxHeap()
    for v in [5, 3, 8, 1, 2]:
        h.push(v)
    print([h.pop() for _ in range(5)])
