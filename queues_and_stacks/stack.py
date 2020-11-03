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

    def is_empty(self):
        if self.data is None:
            return True
        return False

    def peek(self):
        if self.data:
            return self.data[-1]
        else:
            return "Stack is empty"


class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data} --> {self.next}'


class StackWithLL:
    def __init__(self):
        self.top = None

    def __str__(self):
        return f'{self.top}'

    def push(self, item):
        # Create a new Node
        new_node = LinkedListNode(item)
        # set current top to new_node's next
        new_node.next = self.top
        # reset the top pointer to the new node
        self.top = new_node

    def pop(self):
        # store the popped node
        data = self.top.data
        # check if the stack is empty
        if self.is_empty() == False:
            # reset top pointer to next node
            self.top = self.top.next
            # return the value from the popped node
            return data

    def is_empty(self):
        if self.top is None:
            return True
        return False

    def peek(self):

        return self.top.data
        # current = self.top.data

        # while current.next is not None:
        #     current = current.next

        # return current


s = StackWithLL()
s.push(5)
s.push(6)
s.push(7)
print(s)
print(s.peek())
print(s.pop())
print(s)
