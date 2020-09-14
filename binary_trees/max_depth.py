'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''


def max_depth(root):
    if not root:
        return 0

    if root.left is None and root.right is None:
        return 1

    left = 1 + max_depth(root.left)
    right = 1 + max_depth(root.right)

    return max(left, right)
