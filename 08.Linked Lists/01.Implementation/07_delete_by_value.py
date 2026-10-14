class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_value(head, value):
    dummy = Node(0)
    dummy.next = head
    curr = dummy
    while curr.next:
        if curr.next.data == value:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head = delete_value(head, 2)
    while head:
        print(head.data, end=" ")
        head = head.next
