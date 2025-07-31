# A linked list (LL) node 
# to store a queue entry 
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    #Function to push an element into the queue.
    def push(self, item): 
    
         #Add code here
        newnode = Node(item)
        if self.tail is None:
            self.head = self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
         
    
    #Function to pop front element from the queue.
    def pop(self):
         
         #add code here
        if self.head is None:
            return -1
        x = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return x