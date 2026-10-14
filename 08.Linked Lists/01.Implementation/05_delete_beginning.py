class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_beginning(head):
    if not head:
        return None
    return head.next


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head = delete_beginning(head)
    print(head.data)
