class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self):
        return f'{self.val}'


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        curr = self.head

        for _ in range(index + 1):
            curr = curr.next
        return curr.val

    def listLength(self):
        current = self.head
        length = 0
        while current is not None:
            length += 1
            current = current.next
        return length

    # different way w/o recursion

    def insertHead(self, newNode):
        tempHead = self.head
        self.head = newNode
        newNode.next = tempHead
        del tempHead

    def add_at_head(self, val):
        self.add_at_index(0, val)

    def add_at_tail(self, val):
        self.add_at_index(self.size, val)

    # One w/o using self.size / recursion
    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            last = self.head
            while True:
                if last.next is None:
                    break
                last = last.next
            last.next = newNode

    def add_at_index(self, index, val):
        if index > self.size:
            return
        if index < 0:
            index = 0

        self.size += 1

        prev = self.head

        for _ in range(index):
            prev = prev.next

        add_node = Node(val)
        add_node.next = prev.next
        prev.next = add_node

    def insert(self, newNode, position):
        # head=>10->20->None || newNode=>15->None  || position=> 1
        if position < 0 or position > self.listLength():
            print("Invalid position")
            return
        if position == 0:
            self.insertHead(newNode)
            return
        current = self.head
        prevNode = current
        currentPosition = 0
        while True:
            if currentPosition == position:
                prevNode.next = newNode
                newNode.next = current
                break

            current = current.next
            currentPosition += 1

    # another way to delete end node
    def deleteEnd(self):
        # head=> jon->luke->mark->None
        last = self.head
        while last.next is not None:
            prev = last
            last = last.next
        prev.next = None

    def deleteIndex(self, position):
        # head=>jon->luke->mark->None || position 1

        if position < 0 or position >= self.listLength():
            print('Invalid position')
            return
        if self.isListEmpty() is False:
            if position == 0:
                self.deleteEnd()
                return

            current = self.head
            prev = current
            currentPosition = 0
            while True:
                if currentPosition == position:
                    prev.next = current.next
                    current.next = None
                    break
                current = current.next
                currentPosition += 1

    def isListEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def delete_at_index(self, index):
        if index < 0 or index >= self.size:
            return

        self.size -= 1

        prev = self.head

        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next

    def printList(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while True:
            if current is None:
                break
            print(f'{current.val} -> ', end='')
            current = current.next
        print('None')


def mergeLists(firstList, secondList, mergedList):
    # 1->3->4 || 2->7->9 || 1->2->3->4 None
    currentFirst = firstList.head
    currentSecond = secondList.head
    while True:
        if currentFirst is None:
            mergedList.insertEnd(currentSecond)
            break
        if currentSecond is None:
            mergedList.insertEnd(currentFirst)
            break
        if currentFirst.val < currentSecond.val:
            currentFirstNext = currentFirst.next
            currentFirst.next = None
            mergedList.insertEnd(currentFirst)
            currentFirst = currentFirstNext
        else:
            currentSecondNext = currentSecond.next
            currentSecond.next = None
            mergedList.insertEnd(currentSecond)
            currentSecond = currentSecondNext


one = Node(1)
two = Node(3)
three = Node(4)
firstList = LinkedList()
firstList.insertEnd(one)
firstList.insertEnd(two)
firstList.insertEnd(three)

four = Node(2)
five = Node(7)
six = Node(9)
secondList = LinkedList()
secondList.insertEnd(four)
secondList.insertEnd(five)
secondList.insertEnd(six)

print("Printing first List")
firstList.printList()
print("Printing second list")
secondList.printList()


mergedList = LinkedList()

mergeLists(firstList, secondList, mergedList)
del firstList
del secondList

print("Printing Merged List")
mergedList.printList()
