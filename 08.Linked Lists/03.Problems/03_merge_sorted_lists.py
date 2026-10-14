class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_sorted(l1, l2):
    dummy = Node(0)
    tail = dummy
    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next


if __name__ == "__main__":
    a = Node(1)
    a.next = Node(3)
    a.next.next = Node(5)
    b = Node(2)
    b.next = Node(4)
    b.next.next = Node(6)
    head = merge_sorted(a, b)
    while head:
        print(head.data, end=" ")
        head = head.next
