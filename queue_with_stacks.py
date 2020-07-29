'''
https://leetcode.com/problems/implement-queue-using-stacks/

Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
'''


class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def print_stack(self):
        print(f'Input Stack: {self.input}')
        print(f'Output Stack: {self.output}')

    def push(self, x):
        self.input.append(x)

    def move_to_output(self):
        if not self.output:
            while self.input:
                popped = self.input.pop()
                self.output.append(popped)

    def pop(self):
        self.move_to_output()
        self.print_stack()
        return self.output.pop()

    def peek(self):
        self.move_to_output()
        self.print_stack()
        return self.output[-1]

    def empty(self):
        if not self.input and not self.output:
            self.print_stack()
            return True

        return False


x = [[], [1], [2], [], [], []]
obj = MyQueue()
print(obj.push(x))
print(obj.pop())
print(obj.peek())
print(obj.empty())
