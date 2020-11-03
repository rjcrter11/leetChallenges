class Stack:
    def __init__(self):
        self.data = []

    def __str__(self):
        return f'{self.data}'

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) > 0:
            self.data.pop()
        return 'The stack is empty'

    def peek(self):
        if self.data:
            return self.data[-1]
        else:
            return "Stack is empty"


class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackWithLL:
    def __init__(self):
        self.top = None

    def push(self, item):
        # Create a new Node
        new_node = LinkedListNode(item)
        # set current top to new_node's next
        new_node.next = self.top
        # reset the top pointer to the new node
        self.top = new_node

    def pop(self):
        # check if the stack is empty
        if self.top is not None:
            # store the popped node
            popped = self.top
            # reset top pointer to next node
            self.top = popped.next
            # return the value from the popped node
            return popped.data

    def peek(self):
        current = self.top

        while current.next is not None:
            current = current.next
        peeked = current
        return peeked.data
