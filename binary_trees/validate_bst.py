'''
Write a function that takes in a potentially invalid BST and returns a boolean 
representing whether the bst is valid
'''


class BST:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def validateBST(tree):
    return validationHelper(tree, float("-inf"), float("inf"))


def validationHelper(tree, minVal, maxVal):
    if tree is None:
        return True

    if tree.value < minVal or tree.value >= maxVal:
        return False

    validLeft = validationHelper(tree.left, minVal, tree.value)
    return validLeft and validationHelper(tree.right, tree.value, maxVal)
