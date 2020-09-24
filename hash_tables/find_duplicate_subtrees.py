

from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubTrees(self, root):
        if not root:
            return None

        result = []
        subtrees = defaultdict(int)

        def divideTrees(node):
            if not node:
                return '#'

            left = divideTrees(node.left)
            right = divideTrees(node.right)
            tree = "{},{},{}".format(node.val, left, right)
            if subtrees[tree] == 1:
                result.append(node)
            subtrees[tree] += 1
            return tree

        divideTrees(root)

        return result
