class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        count = 0
        temp = self.head
        while temp is not None:
            if count == index:
                return temp.val
            temp = temp.next
            count += 1
        return -1  

    def addAtHead(self, val: int) -> None:
        newnode = Node(val)
        newnode.next = self.head
        self.head = newnode  #perfect
 
    def addAtTail(self, val: int) -> None:
        newnode = Node(val)
        if not self.head:
            self.head = newnode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        newnode = Node(val)
        count = 0
        curr = self.head
        prev = None

        while curr and count < index:
            prev = curr
            curr = curr.next
            count += 1

        if count == index:
            prev.next = newnode
            newnode.next = curr
        # Else: index > length, do nothing

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return

        if index == 0:
            self.head = self.head.next
            return

        temp = self.head
        count = 0

        while temp and temp.next:
            if count == index - 1:
                temp.next = temp.next.next
                return
            temp = temp.next
            count += 1
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
