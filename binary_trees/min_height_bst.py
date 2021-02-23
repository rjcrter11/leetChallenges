'''
Write a function that takes in a non-empty sorted array of distint integers, contructs
a BST from them, and returns the root of the BST.
The function should minimize the height of the BST.

array = [1,2,5,7,10,13,14,15,22]
output =            10
                  /    \
                2       14
               / \     /  \
              1   5   13   15
                   \         \
                    7        22
'''


def minHeightBst(array):
    return constructMinHeight(array, 0, len(array)-1)


def constructMinHeight(array, start, end):
    if end < start:
        return None
    mid = (start + end) // 2
    bst = BST(array[mid])
    bst.left = constructMinHeight(array, start, mid-1)
    bst.right = constructMinHeight(array, mid+1, end)
    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
