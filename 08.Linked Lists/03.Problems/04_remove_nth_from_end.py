class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    slow = fast = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head = remove_nth_from_end(head, 2)
    while head:
        print(head.data, end=" ")
        head = head.next
