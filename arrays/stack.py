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
        if len(self.data) > 0:
            print(self.data[-1])

        if len(self.data) == 0:
            return
