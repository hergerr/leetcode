class Node:
    def __init__(self, value, prev, nxt) -> None:
        self.value = value
        self.prev = prev
        self.nxt = nxt

class MyLinkedList:

    def __init__(self):
        # to avoid edge cases
        self.head = Node(-1, None, None)
        self.tail = Node(-1, self.head, None)
        self.head.nxt = self.tail
        self.size = 0

    def findNode(self, index) -> Node:
        if index < 0 or self.size == 0 or index:
            return
        counter = 0
        node = self.head.nxt
        while counter < index:
            counter += 1
            node = node.nxt
            if not node.nxt:
                return
        return node

    def get(self, index: int) -> int:
        node = self.findNode(index)
        if not node:
            return -1
        return node.value

    def addAtHead(self, val: int) -> None:
        new_node = Node(val, self.head, self.head.nxt)
        self.head.nxt.prev = new_node
        self.head.nxt = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val, self.tail.prev, self.tail)
        self.tail.prev.nxt = new_node
        self.tail.prev = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        node = self.findNode(index)
        if index == self.size:
            self.addAtTail(val)
            return

        if not node:
            return
        
        new_node = Node(val, node.prev, node)
        node.prev.nxt = new_node
        node.prev = new_node
        self.size += 1
        


    def deleteAtIndex(self, index: int) -> None:
        node = self.findNode(index)
        if not node:
            return
        
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev


# Your MyLinkedList object will be instantiated and called as such:
myLinkedList = MyLinkedList()
print(myLinkedList.addAtTail(0))
print(myLinkedList.addAtTail(1))
print(myLinkedList.addAtTail(2))
print(myLinkedList.addAtTail(3))
print(myLinkedList.addAtIndex(2, 100))
print(myLinkedList.get(0))
print(myLinkedList.get(1))
print(myLinkedList.get(2))
print(myLinkedList.get(3))
print(myLinkedList.get(4))
print(myLinkedList.get(5))
