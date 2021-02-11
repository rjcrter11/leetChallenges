'''
Write a function that takes in a BST and a target int value and returns the closest value
to that target value contained in the BST.
You can assume that there will only be one closest value.

tree =      10
          /    \
        5       15
       / \      / \
      2   5    13 22
     /          \ 
    1           14

target = 12 
output = 13
'''


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findClosestValueInBst(tree, target):
    currentNode = tree
    currentClosest = currentNode.value

    while currentNode is not None:
        if abs(target - currentClosest) > abs(target - currentNode.value):
            currentClosest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left

        if target > currentNode.value:
            currentNode = currentNode.right
        else:
            return currentClosest
    return currentClosest
