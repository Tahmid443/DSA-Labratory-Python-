class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at(head, pos, data):
    new = Node(data)
    if pos == 0:
        new.next = head
        return new
    curr = head
    for _ in range(pos - 1):
        if not curr:
            return head
        curr = curr.next
    if curr:
        new.next = curr.next
        curr.next = new
    return head


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(4)
    head = insert_at(head, 2, 3)
    while head:
        print(head.data, end=" ")
        head = head.next
