'''
You're given a Node class that has a name and an array of optional children nodes. When put
together, nodes form an acyclic tree-like structure.
Implement the breadthFirstSearch method on the Node class, which takes an empty array, traverse
the tree using the BFS approach, stores all of the nodes' names in the input array,
and returns it.
'''


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        q = [self]

        while q:
            current = q.pop(0)
            array.append(current.name)

            for child in current.children:
                q.append(child)

        return array
