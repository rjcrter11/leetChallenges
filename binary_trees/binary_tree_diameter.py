'''
Write a function that takes in a BST and returns its diamter. The diamter of a binary
tree is defined as the length of its longest path, even if that path doesn't pass 
through the root of the tree.
A path is a collection of connected nodes in a tree, where no node is connected to more
that two other nodes. The length of a path is the number of edges between the path's
first node and its last node. 
'''


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter


def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0)

    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    longestPath = leftTreeInfo.height + rightTreeInfo.height
    maxDiameterNow = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
    currentDiameter = max(longestPath, maxDiameterNow)
    currentHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)

    return TreeInfo(currentDiameter, currentHeight)


class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height
