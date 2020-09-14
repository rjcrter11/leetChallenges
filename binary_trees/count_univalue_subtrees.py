'''
Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.

 

Example 1:

       5
     /  \
    1    5
   / \    \
  5   5    5



Input: root = [5,1,5,5,5,null,5]
Output: 4
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.count = 0
        self.is_unival(root)
        return self.count

    def is_unival(self, node):
        if not node.left and not node.right:
            self.count += 1
            return True
        is_uni = True

        if node.left is not None:
            is_uni = self.is_unival(
                node.left) and is_uni and node.left.val == node.val

        if node.right is not None:
            is_uni = self.is_unival(
                node.right) and is_uni and node.right.val == node.val

        self.count += is_uni
        return is_uni
