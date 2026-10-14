class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_end(head):
    if not head or not head.next:
        return None
    curr = head
    while curr.next.next:
        curr = curr.next
    curr.next = None
    return head


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head = delete_end(head)
    while head:
        print(head.data, end=" ")
        head = head.next
