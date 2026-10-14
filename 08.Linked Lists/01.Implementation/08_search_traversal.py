class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def search(head, target):
    curr, idx = head, 0
    while curr:
        if curr.data == target:
            return idx
        curr = curr.next
        idx += 1
    return -1


def traverse(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    traverse(head)
    print(search(head, 2))
