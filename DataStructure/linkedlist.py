class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def insertStart(self, data):
        self.size = self.size +1
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    def linkedListSize(self):
        return self.size

    def insertEnd(self, data):
        self.size = self.size + 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.next is not None:
            actualNode = actualNode.next
            actualNode.next = newNode
    def traverseList(self):
        currentNode = self.head

        while currentNode is not None:
            print currentNode.data
            currentNode = currentNode.next
    def remove(self, data):
        if self.head is None:
            return
        currentNode = self.head
        previousNode = None
        while currentNode.data is not data:
            previousNode = currentNode
            currentNode = currentNode.next
#this if statement removes head node
        if previousNode is None:
            self.head = currentNode.next
        else:
            previousNode.next = currentNode.next


linkedList = linkedList()
linkedList.insertStart(2)
linkedList.insertStart(21)
linkedList.insertStart(211)
print "HELLO"
linkedList.traverseList()
