#User function Template for python3


# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def __init__(self):
        self.head = None
    def constructDLL(self, arr):
        # Code here
        if not arr:
            return None

        self.head = Node(arr[0])
        current = self.head

        for value in arr[1:]:
            new_node = Node(value)
            current.next = new_node   
            new_node.prev = current   
            current = new_node 

        return self.head