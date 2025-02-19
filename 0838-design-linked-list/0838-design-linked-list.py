class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MyLinkedList:

    def __init__(self):
        self.dummy = Node()
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        currIdx = 0
        currNode = self.dummy.next

        while currIdx < index:
            currNode = currNode.next
            currIdx += 1

        return currNode.val

    def addAtHead(self, val: int) -> None:
        head =  self.dummy.next
        new_node = Node(val)
        self.dummy.next = new_node
        new_node.next = head

        if not self.tail:
            self.tail = new_node

        self.length += 1
    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.tail:
            self.dummy.next = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return 
        if index == self.length:
            self.addAtTail(val)
        else:
            currIdx = 0
            currNode = self.dummy

            while currIdx < index:
                currNode = currNode.next
                currIdx += 1
            new = Node(val)
            new.next = currNode.next
            currNode.next = new

            self.length += 1        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        
        currIdx = 0
        currNode = self.dummy

        while currIdx < index:
            currNode = currNode.next
            currIdx += 1
        
        currNode.next = currNode.next.next

        if not currNode.next:
            self.tail = currNode

        self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)