class CircularQueue:
    def __init__(self, k):
        self.data = []
        self.capacity = [0] * k
        self.count = 0
        self.head = 0

    def enQueue(self, value):
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
