import Node
class List(object):
    def __init__(self, head):
        self.length = 0
        self.head = None
        self.tail = None

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def add(self, value):
        node = Node(value);
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            node.prev=self.tail
            self.tail=node

    def remove(self, value):
        currentElement=self.head
        while currentElement is not None:
            if currentElement.value ==  value:
                currentElement.prev.next=currentElement.next
                currentElement.next.prev=currentElement.prev
                del currentElement
                return True
        return False

    def Serch(self, value):
        currentElement=self.head
        while currentElement is not None:
            if currentElement.value == value:
                return True
        return False









