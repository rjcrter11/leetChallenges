'''
You're given the head of a Singly Linked List whose nodes are in sorted order with 
respect to their values. Write a function that returns a modified version of the LL that doesn't
contain any nodes with duplicate values. The LL should be modified in place, and the modified
LL should still have its nodes sorted with respect to their values.

linkedList = 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6
output 1 -> 3 -> 4 -> 5 -> 6
'''


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicates(linkedList):
    currentNode = linkedList

    while currentNode is not None:
        nextNode = currentNode.next
        while nextNode is not None and nextNode.value == currentNode.value:
            nextNode = nextNode.next
        currentNode.next = nextNode
        currentNode = nextNode
    return linkedList
