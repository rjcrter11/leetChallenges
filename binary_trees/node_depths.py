'''
The distance between a node in a BT and the tree's root is called the node's depth.
Write a function that takes in a BT and returns the sum of its nodes' depths.

'''


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def nodeDepths(root, depth=0):
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)
