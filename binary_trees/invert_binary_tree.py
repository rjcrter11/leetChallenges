'''
Write a function that takes in a BST and inverts it. In other words, the function 
should swap every left node in the tree for its corresponding right node.
'''


def invertBinaryTree(tree):

    if tree is None:
        return
    swap(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


def swap(tree):
    tree.left, tree.right = tree.right, tree.left


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left - None
        self.right = None
