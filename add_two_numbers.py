'''
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        sum = l1.val + l2.val
        carry = sum // 10
        sum_list = ListNode(sum % 10)
        p1 = l1.next
        p2 = l2.next
        p3 = sum_list

        while p1 or p2:
            if p1:
                value_one = p1.val
            else:
                value_one = 0
            if p2:
                value_two = p2.val
            else:
                value_two = 0
            sum = value_one + value_two + carry
            carry = sum // 10
            p3.next = ListNode(sum % 10)
            p3 = p3.next
            if p1:
                p1 = p1.next
            else:
                p1 = None
            if p2:
                p2 = p2.next
            else:
                p2 = None

        if (carry > 0):
            p3.next = ListNode(carry)
        return sum_list
