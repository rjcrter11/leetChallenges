'''
https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1215/

Write a program to find the node at which the intersection of two singly linked lists begins.
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the 
two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, 
it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; 
There are 3 nodes before the intersected node in B.
'''


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
