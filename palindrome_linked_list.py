class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def get_midpoint(self, head):
        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    def reverse(self, head):

        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def is_palindrome(self, head):

        if head is None:
            return True

        first_half_end = self.get_midpoint(head)
        second_half_start = self.reverse(first_half_end.next)

        palindrome = True

        first = head
        second = second_half_start

        while palindrome and second:
            if first.val != second.val:
                palindrome = False

            first = first.next
            second = second.next

        first_half_end.next = self.reverse(second_half_start)
        return palindrome
