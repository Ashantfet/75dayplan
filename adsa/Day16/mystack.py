class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Function to push an integer into the stack.
    def push(self,data):
        #add code here
        self.arr.append(data)
    
    #Function to remove an item from top of the stack.
    def pop(self):
        #add code here
        if len(self.arr) == 0:
            return -1
        x = self.arr.pop()
        return x
        
