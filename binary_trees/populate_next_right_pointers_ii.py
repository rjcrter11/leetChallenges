'''
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
 

Example 1:



Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer 
to point to its next right node, just like in Figure B. The serialized output is in level order as 
connected by the next pointers, with '#' signifying the end of each level.
'''


class Node:
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):

        if not root:
            return root

        q = [root]

        while q:
            size = len(q)

            for i in range(size):
                node = q.pop(0)

                if i < size-1:
                    node.next = q[0]

                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

        return root
