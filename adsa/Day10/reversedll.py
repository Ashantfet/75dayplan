
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


class Solution:
    def reverseDLL(self, head):
        #return head of reverse doubly linked list
        if head.next is None:
            return head
        curr = head
        prev =None
        while curr:
            front = curr.next
            curr.next = prev
            curr.prev = front
            prev = curr
            curr = front
        return prev