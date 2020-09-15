'''
Serialization is the process of converting a data structure or object into a sequence 
of bits so that it can be stored in a file or memory buffer, or transmitted 
across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. 
You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ''
        q = []
        q.append(root)
        result = ''

        while q:
            node = q.pop(0)
            if not node:
                result += 'None,'
                continue
            result += str(node.val) + ','
            q.append(node.left)
            q.append(node.right)
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if not data:
            return None

        ls = data.split(',')
        root = TreeNode(int(ls[0]))
        q = []
        q.append(root)
        i = 1
        while q and i < len(ls):
            node = q.pop(0)
            if ls[i] != 'None':
                left = TreeNode(int(ls[i]))
                node.left = left
                q.append(left)
            i += 1
            if ls[i] != "None":
                right = TreeNode(int(ls[i]))
                node.right = right
                q.append(right)
            i += 1
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
