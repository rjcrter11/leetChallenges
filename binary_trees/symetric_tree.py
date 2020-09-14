'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 
'''
# recursive


def is_symetric(root):
    return is_mirror(root, root)


def is_mirror(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False

    return t1.val == t2.val and is_mirror(t1.right, t2.left) and is_mirror(t1.left and t2.right)


# iterative

def is_symetric_iterative(root):
    if not root:
        return True

    left = []
    right = []
    s1 = [root.left]
    s2 = [root.right]

    while s1 and s2:
        n1 = s1.pop()
        n2 = s2.pop()

        if not n1 or not n2:
            if not n1 and not n2:
                continue
            else:
                return False

        if n1.val != n2.val:
            return False

        left.append(n1)
        right.append(n2)

        if n1.left:
            s1.append(n1.left)
        if n1.right:
            s1.append(n1.right)
        if n2.left:
            s2.append(n2.left)
        if n2.right:
            s2.append(n2.right)

    if s1 or s2:
        return False
    return True
