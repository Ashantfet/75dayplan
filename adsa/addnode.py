class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None


class Solution:
    #Function to insert a new node at given position in doubly linked list.
    def addNode(self, head, p, x):
        # Code here
        newnode = Node(x)
        if p == 0:
            if not head:
                head = newnode
            else:
                newnode.next = head
                head.prev = newnode
                head = newnode
            return
        else:
            current = head
            count = 0
            while current and count <p:
                current = current.next
                count +=1
            if current is None:
                return -1
            newnode.next = current.next
            newnode.prev = current
            if current.next:
                current.next.prev = newnode
            current.next = newnode
            return head
                