class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_end(head, data):
    new = Node(data)
    if not head:
        return new
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new
    return head


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head = insert_end(head, 3)
    while head:
        print(head.data, end=" ")
        head = head.next
