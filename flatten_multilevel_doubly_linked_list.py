'''
https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1225/

You are given a doubly linked list which in addition to the next and previous pointers, 
it could have a child pointer, which may or may not point to a separate doubly linked list. 
These child lists may have one or more children of their own, and so on, to produce 
a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, 
doubly linked list. You are given the head of the first level of the list.
'''


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
