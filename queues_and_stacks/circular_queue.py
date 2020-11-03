class CircularQueue:
    def __init__(self, k):
        self.data = []
        self.capacity = [0] * k
        self.count = 0
        self.head = 0

    def enQueue(self, value):
        # use modulu b/c the remainder will give the correct next index
        if self.isFull():
            return False
        self.data[(self.head + self.count) % self.capacity] = value
        self.count += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def front(self):
        if self.count == 0:
            return -1
        return self.data[self.head]

    def rear(self):
        if self.count == 0:
            return -1
        return self.data[(self.head + self.count - 1) % self.capacity]

    def isEmpty(self):
        if self.count == 0:
            return True
        return False

    def isFull(self):
        if self.count == self.capacity:
            return True
        return False


class circQueue2:
    def __init__(self, k):
        self.queue = [None] * k
        self.head = 0
        self.tail = -1
        self.capacity = k
        self.q_size = 0

    def enqueue(self, value):
        if self.is_full:
            return False
        self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = value
        self.q_size += 1
        return True

    def dequeue(self):

        if self.is_empty():
            return False
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.q_size -= 1
        return True

    def front(self):
        return -1 if self.is_empty() else self.queue[self.head]

    def rear(self):
        return -1 if self.is_empty() else self.queue[self.tail]

    def is_full(self):
        return self.q_size == self.capacity

    def is_empty(self):
        return self.q_size == 0
