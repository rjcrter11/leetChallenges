class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head):
        if not head:
            return

        pseudo = Node(0, None, head, None)
        prev = pseudo

        stack = []
        stack.append(head)

        while stack:
            curr = stack.pop()

            prev.next = curr
            curr.prev = prev

            if curr.next:
                stack.append(curr.next)

            if curr.child:
                stack.append(curr.child)
                curr.child = None

            prev = curr

        pseudo.next.prev = None

        return pseudo.next
