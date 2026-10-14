class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_beginning(head, data):
    new = Node(data)
    new.next = head
    return new


if __name__ == "__main__":
    head = Node(2)
    head.next = Node(3)
    head = insert_beginning(head, 1)
    while head:
        print(head.data, end=" ")
        head = head.next
