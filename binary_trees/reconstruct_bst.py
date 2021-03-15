'''
The pre-order traversal of a BST is a traversal technique that starts at the tree's root node and visits
nodes in the following order:
    1. Current node
    2. Left subtree
    3. Right subtree
Given a non-empty array of integers representing the pre-order traversal of a BST, write a function
that creates the relevant BST and returns its root node
'''


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preorderValues):
    if len(preorderValues) == 0:
        return None

    current = preorderValues[0]
    rightRootIdx = len(preorderValues)

    for i in range(1, len(preorderValues)):
        value = preorderValues[i]
        if value >= current:
            rightRootIdx = i
            break
    leftSubTree = reconstructBst(preorderValues[1:rightRootIdx])
    rightSubTree = reconstructBst(preorderValues[rightRootIdx:])

    return BST(current, leftSubTree, rightSubTree)


values = [10, 4, 2, 1, 5, 17, 19, 18]


print(reconstructBst(values))
