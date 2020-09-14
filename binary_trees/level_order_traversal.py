'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''


def level_order(root):

    tiers = []

    if not root:
        return tiers

    tier = 0

    q = []
    q.append(root)

    while q:
        tiers.append([])
        tier_length = len(q)

        for _ in range(tier_length):
            node = q.pop(0)
            tiers[tier].append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        tier += 1
    return tiers
