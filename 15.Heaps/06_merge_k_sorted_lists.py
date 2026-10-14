import heapq


class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def merge_k_lists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    dummy = Node(0)
    tail = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next


if __name__ == "__main__":
    a = Node(1)
    a.next = Node(4)
    a.next.next = Node(5)
    b = Node(1)
    b.next = Node(3)
    b.next.next = Node(4)
    c = Node(2)
    c.next = Node(6)
    head = merge_k_lists([a, b, c])
    while head:
        print(head.val, end=" ")
        head = head.next
