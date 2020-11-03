class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data} '


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def __str__(self):
        return f'{self.front} --> {self.rear}'

    def enqueue(self, item):
        new_node = LinkedList(item)
        # check if queue is empty
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            # add new node to rear
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        # check if queue is empty
        if self.front is not None:
            # keep copy of old front
            old_front = self.front
            # set new front
            self.front = old_front.next
        # check if queue is now empty
        if self.front is None:
            self.rear = None

        return old_front

    def is_empty(self):
        if self.front is None:
            return True
        return False

    def peek(self):
        peeked = self.front
        if self.front is not None:
            return peeked.data
        return "Queue is empty"


class QueueArray():
    def __init__(self):
        self.data = []

    def __str__(self):
        return f'{self.data}'

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if len(self.data) > 0:
            self.data.pop(0)
        else:
            return "The queue is empty"

    def peek(self):
        if self.data:
            return self.data[0]
        return "The queue is empty"

    def is_empty(self):
        if self.data is None:
            return True
        return False
