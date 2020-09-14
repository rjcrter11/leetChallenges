

def preorder_traversal(root):
    stack = []
    stack.append(root)
    result = []

    if root is None:
        return []

    while stack:
        current = stack.pop()
        result.append(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return result
