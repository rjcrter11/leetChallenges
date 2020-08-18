class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def has_cycle(self, head):

        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True
        return False
