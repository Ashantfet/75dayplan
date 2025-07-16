class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Solution:
    def insertAtEnd(self, head, x):
        
        new_node = Node(x)
        if head == None:
            new_node.next = head
            head = new_node
        else:
            
            curr = head
            prev = None
            while curr is not None:
                prev = curr
                curr = curr.next
            prev.next = new_node
            new_node.next = curr
        
        return head

head = None
n = int(input())
for _ in range(n):
    x = int(input())
    sol = Solution()
    head = sol.insertAtEnd(head, x)
current = head
while current:
    print(current.data, end=" ")
    current = current.next
print()