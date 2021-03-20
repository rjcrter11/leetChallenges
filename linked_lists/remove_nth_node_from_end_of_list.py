class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def remove_nth(self, head, n):

        slow = head
        fast = head

        if n == 0:
            return head

        for i in range(n):
            if fast.next == None:
                if i == n-1:
                    head = head.next
                return head
            fast = fast.next

        while fast.next != None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head


def remove_nthAlt(head, k):

    count = 1
    fast = head
    slow = head

    while count <= k:
        fast = fast.next
        count += 1
    if fast is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while fast.next is not None:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
