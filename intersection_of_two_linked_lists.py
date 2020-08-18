class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def get_intersection_node(self, headA, headB):

        if headA is None or headB is None:
            return None

        pointer_a = headA
        pointer_b = headB

        while pointer_a != pointer_b:
            pointer_a = headB if pointer_a is None else pointer_a.next
            pointer_b = headA if pointer_b is None else pointer_b.next

        return pointer_a
