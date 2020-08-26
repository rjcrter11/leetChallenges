class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node(0)

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        curr = self.head

        for _ in range(index + 1):
            curr = curr.next
        return curr.val

    def add_at_head(self, val):
        self.add_at_index(0, val)

    def add_at_tail(self, val):
        self.add_at_index(self.size, val)

    def add_at_index(self, index, val):
        if index > self.size:
            return
        if index < 0:
            index = 0

        self.size += 1

        prev = self.head

        for _ in range(index):
            prev = prev.next

        add_node = Node(val)
        add_node.next = prev.next
        prev.next = add_node

    def delete_at_index(self, index):
        if index < 0 or index >= self.size:
            return

        self.size -= 1

        prev = self.head

        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next
