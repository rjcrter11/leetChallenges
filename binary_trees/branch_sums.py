'''
Write a function that takes in a Binary Tree and returns a list of its branch sums
ordered from leftmost branch sum to rightmost branch sum.
A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree 
branch is a path of nodes in a tree that starts at the root node and ends
at any leaf node
'''


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    sumsHelper(root, 0, sums)
    return sums


def sumsHelper(node, runningSum, sums):
    if node is None:
        return

    newSum = runningSum + node.value

    if node.left is None and node.right is None:
        sums.append(newSum)
        return

    sumsHelper(node.left, newSum, sums)
    sumsHelper(node.right, newSum, sums)
