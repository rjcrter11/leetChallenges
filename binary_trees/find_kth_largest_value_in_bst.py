'''
Write a function that takes in a BST and a positive integer k and returns the largest integer
contained in the BST.
'''


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_kth_largest_value(tree, k):
    current = tree
    stack = []
    array = []

    while current or stack:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            array.append(current.value)
            current = current.right

    return array[-k]
