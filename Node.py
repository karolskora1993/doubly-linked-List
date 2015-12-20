class Node(object):
    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.prev = None
    def hasNext(self):
        if self.next is not None:
            return True
        else:
            return False
    def hasPrev(self):
        if self.prev is not None:
            return True
        else:
            return False
    def getNext(self):
        return self.next
    def getPrev(self):
        return self.prev

