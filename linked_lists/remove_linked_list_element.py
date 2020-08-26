'''
https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1207/

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val}'


class Solution:
    def remove_elements(self, head, val):

        curr = head
        prev = None

        while curr:
            if curr.val == val:
                if prev and head:
                    prev.next = curr.next
                    curr.next = None
                    curr = prev.next
                else:
                    head = head.next
                    curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return head
