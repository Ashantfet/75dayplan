class MyStack:


    class StackNode:

    # Constructor to initialize a node
        def __init__(self, data):
            self.data = data
            self.next = None
    def __init__(self):
        self.head =None
        
    #Function to push an integer into the stack.
    def push(self, data):
        newnode = MyStack.StackNode(data)
        newnode.next = self.head
        self.head = newnode
        
    #Function to remove an item from top of the stack.
    def pop(self):

        # Add code here
        if self.head is None:
            return -1
        x =self.head.data
        self.head = self.head.next
        return x