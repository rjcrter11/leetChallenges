class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Solution:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index):
        if index < 0 or index > self.size:
            return -1

        if index + 1 < self.size - index:
            curr = self.head

            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail

            for _ in range(self.size - index):
                curr = curr.prev

        return curr.val

    def add_at_head(self, val):
        pred = self.head
        succ = self.head.next

        self.size += 1

        add = ListNode(val)
        add.prev = pred
        add.next = succ
        pred.next = add
        succ.prev = add

    def add_at_tail(self, val):

        pred = self.tail
        succ = self.tail.prev

        self.size += 1

        add = ListNode(val)
        add.prev = pred
        add.next = succ
        pred.next = add
        succ.prev = add

    def add_at_index(self, index, val):

        if index > self.size:
            return

        if index < 0:
            index = 0

        if index < self.size - index:
            pred = self.head

            for _ in range(index):
                pred = pred.next
            succ = pred.next

        else:
            succ = self.tail

            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev

        self.size + 1
        add = ListNode(val)
        add.prev = pred
        add.next = succ
        pred.next = add
        succ.prev = add

    def delete_at_index(self, index):

        if index < 0 or index >= self.size:
            return

        if index < self.size - index:
            pred = self.head

            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail

            for _ in range(self.size - index-1):
                succ = succ.prev
            pred = succ.prev.prev

        self.size -= 1
        pred.next = succ
        succ.prev = pred
