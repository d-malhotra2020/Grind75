class ListNode:
    def __init__(self, val):
        self.val = val
        self.previous = None
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.previous = self.left

    def get(self, index: int) -> int:
        current = self.left.next
        while current and index > 0:
            current = current.next
            index -=1
        if current and current != self.right and index == 0:
            return current.val
        return -1

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        next = self.left.next
        previous = self.left
        previous.next = node
        next.previous = node
        node.next = next
        node.previous = previous

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        next = self.right
        previous = self.right.previous
        previous.next = node
        next.previous = node
        node.next = next
        node.previous = previous

    def addAtIndex(self, index: int, val: int) -> None:
        current = self.left.next
        while current and index > 0:
            current = current.next
            index -=1
        if current and index == 0:
            node = ListNode(val)
            next = current
            previous = current.previous
            previous.next = node
            next.previous = node
            node.next = next
            node.previous = previous
            
    def deleteAtIndex(self, index: int) -> None:
        current = self.left.next
        while current and index > 0:
            current = current.next
            index -=1
        if current and current != self.right and index == 0:
            next = current.next
            previous = current.previous
            next.previous = previous
            previous.next = next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)