class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = next


class Solution:
    def reverse_list(self, head):
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head

        # recursive solution

        # if head == None or head.next == None:
        #     return head

        # rev = self.reverse_list(head.next)
        # head.next.next = head
        # head.next = None
        # return rev
