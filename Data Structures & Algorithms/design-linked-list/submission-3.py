class Node:
        
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        curr = self.head
        count = 0
        while curr != None and count < index:
            count += 1
            curr = curr.next
        
        if curr != None:
            return curr.val
        else:
            return -1
        

    def addAtHead(self, val: int) -> None:
        new = Node(val)

        if self.head == None:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = self.head.prev
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new = Node(val)
        if self.tail == None:
            self.head = new
            self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new
        self.size += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        elif index == self.size:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            count = index
            while count > 0:
                curr = curr.next
                count -= 1
            new = Node(val)
            new.next = curr
            new.prev = curr.prev
            curr.prev.next = new
            curr.prev = new
            self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size or self.size == 0:
            return

        count = index
        curr = self.head
        while count > 0:
            curr = curr.next
            count -= 1
        
        if index == 0 and self.size > 1:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return
        elif index == 0 and self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return
        elif curr.next == None :
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.size -= 1
            return
        
        
        curr.next.prev = curr.prev
        curr.prev.next = curr.next
        self.size -= 1
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)