'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Follow up: Recursive solution is trivial, could you do it iteratively?

 

Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]
'''


def postorder_traversal(root):
    stack = []
    stack.append(root)
    result = []

    while stack:
        current = stack.pop()
        result.append(current.val)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return result[::-1]
