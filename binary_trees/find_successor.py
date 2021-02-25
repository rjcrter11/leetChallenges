'''
Write a function that takes in a BT(where nodes have an additional pointer to their parent node) as
well as a node contained in that tree and returns the given node's successor.
A node's successor is the next node to be visited(immediately after the given node) when traversing
its tree using the inorder tree-traversal technique. A node has no successor if it's the last 
to be visited in the in-order traversal
'''


class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    if node.right is not None:
        return leftmostChild(node.right)
    return rightmostChild(node)


def leftmostChild(node):
    curr = node
    while curr.left is not None:
        curr = curr.left
    return curr


def rightmostChild(node):
    curr = node
    while curr.parent is not None and curr.parent.right == curr:
        curr = curr.right
    return curr.parent
