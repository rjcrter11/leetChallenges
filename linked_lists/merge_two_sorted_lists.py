'''
https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1227/
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        merged_head = None

        if l1.val <= l2.val:
            merged_head = l1
            l1 = l1.next
        else:
            merged_head = l2
            l2 = l2.next

        merged_tail = merged_head

        while l1 != None and l2 != None:
            temp = None
            if l1.val <= l2.val:
                temp = l1
                l1 = l1.next
            else:
                temp = l2
                l2 = l2.next

            merged_tail.next = temp
            merged_tail = temp
        if l1 != None:
            merged_tail.next = l1
        elif l2 != None:
            merged_tail.next = l2
        return merged_head
