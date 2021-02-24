'''
Write a function that takes in a BST and inverts it. In other words, the function 
should swap every left node in the tree for its corresponding right node.
'''


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def invertBinaryTree(tree):

    if tree is None:
        return
    swap(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


def swap(tree):
    tree.left, tree.right = tree.right, tree.left


class BinaryTree2:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def invert2(tree):
    if tree is None:
        return
    temp = tree.left
    tree.left = tree.right
    tree.right = temp
    invert2(tree.left)
    invert2(tree.right)
