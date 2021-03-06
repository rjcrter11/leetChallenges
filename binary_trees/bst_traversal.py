'''
Write three functions that take in a BST and an empty array, traverse the BST, add its
nodes' value to the input array, and return that array. The three functions should 
traverse the BST using the in-order, pre-order, and post-order tree-traversal tequniques.
'''


def inorder(tree, array):
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
    return array


def preorder(tree, array):
    stack = []
    stack.append(tree)
    array = []

    while stack:
        current = stack.pop()
        array.append(current.value)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return array


def postorder(tree, array):
    stack = []
    stack.append(tree)
    array = []

    while stack:
        current = stack.pop()
        array.append(current.value)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return array[::-1]


def inorderRecursive(tree, array):
    if tree is not None:
        inorderRecursive(tree.left, array)
        array.append(tree.value)
        inorderRecursive(tree.right, array)
    return array


def preorderRecursive(tree, array):
    if tree is not None:
        array.append(tree.value)
        preorderRecursive(tree.left, array)
        preorderRecursive(tree.right, array)
    return array


def postorderRecursive(tree, array):
    if tree is not None:
        postorderRecursive(tree.left, array)
        postorderRecursive(tree.right, array)
        array.append(tree.value)
    return array
