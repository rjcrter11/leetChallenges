'''
https://leetcode.com/problems/linked-list-cycle-ii/

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.
'''


# Definition for singly-linked list
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = Nones


def detectCycle(self, head):
    fast = head
    slow = head

    while fast and fast.head:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            seeker = head

            while seeker != slow:
                slow = slow.next
                seeker = seeker.next
            return slow
