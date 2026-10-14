class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            new.next = new
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = new
        new.next = self.head

    def print_list(self):
        if not self.head:
            return
        curr = self.head
        while True:
            print(curr.data, end=" -> ")
            curr = curr.next
            if curr == self.head:
                break
        print("(head)")


if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.append(1)
    cll.append(2)
    cll.append(3)
    cll.print_list()
