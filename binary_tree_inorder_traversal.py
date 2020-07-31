'''
https://leetcode.com/problems/binary-tree-inorder-traversal/

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
'''


# class TreeNode:
#     def __init__(self, val=0, right=None, left=None):
#         self.val = val
#         self.right = right
#         self.left = left


def in_order_traversal(self, root):
    current = root
    stack = []
    result = []

    while current or len(stack) > 0:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            result.append(current.val)
            current = current.right
    return result
