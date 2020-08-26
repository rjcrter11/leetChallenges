'''
https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

Given a node from a Circular Linked List which is sorted in ascending order, 
write a function to insert a value insertVal into the list such that it remains 
a sorted circular list. The given node can be a reference to any single 
node in the list, and may not be necessarily the smallest value in the circular list.

If there are multiple suitable places for insertion, 
you may choose any place to insert the new value. After the insertion, 
the circular list should remain sorted.

If the list is empty (i.e., given node is null), 
you should create a new single circular list and return the reference 
to that single node. Otherwise, you should return the original given node.

'''


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head, insertVal):

        if head == None:
            new_node = ListNode(insertVal, None)
            new_node.next = new_node
            return new_node

        prev = head
        curr = head.next

        insert = False

        while True:
            if prev.val <= insertVal <= curr.val:
                insert = True
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    insert = True

            if insert:
                prev.next = ListNode(insertVal, curr)
                return head

            prev = curr
            curr = curr.next

            if prev == head:
                break
        prev.next = ListNode(insertVal, curr)
        return head
