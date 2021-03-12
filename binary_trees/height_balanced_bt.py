'''
You're given the root node of a BT. Write a function that returns true if the BT is height balanced
and false if it isn't. 
A BT is height balanced if for each node in the tree, the difference between the height of its left 
subtree and the height of its right subtree is at most 1.

'''


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height


def heightBalancedBT(tree):
    treeInfo = getTreeInfo(tree)
    return treeInfo.isBalanced


def getTreeInfo(node):
    if node is None:
        return TreeInfo(True, -1)

    leftSubTreeInfo = getTreeInfo(node.left)
    rightSubTreeInfo = getTreeInfo(node.right)

    isBalanced = (
        leftSubTreeInfo.isBalanced
        and rightSubTreeInfo.isBalanced
        and abs(leftSubTreeInfo.height - rightSubTreeInfo.height) <= 1
    )
    height = max(leftSubTreeInfo.height, rightSubTreeInfo.height) + 1
    return TreeInfo(isBalanced, height)


def heightBalancedBTAlt(tree):
    return isBalancedHelper(tree)[0]


def isBalancedHelper(tree):
    if not tree:
        return True, -1

    leftBalanced, leftHeight = isBalancedHelper(tree.left)

    if not leftBalanced:
        return False, 0

    rightBalanced, rightHeight = isBalancedHelper(tree.right)

    if not rightBalanced:
        return False, 0

    return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)
