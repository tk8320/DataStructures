class Stack:
    def __init__(self) -> None:
        self.list = []
        self.len = 0


    #Prints the whole stack
    def print(self):
        for i in self.list:
            print(i)
    
    #Push the data in Stack
    def push(self,data):
        self.list.append(data)
        self.len += 1
    
    #check if stack is empty or not
    def isEmpty(self):
        if self.len ==0:
            return True 
        else:
            return False 
    
    #pop the item from stack
    def pop(self):
        if self.len == 0:
            return -1
        else:
            self.len -=1
            return self.list.pop()
    
    #trucate the stack
    def truncate(self):
        while not self.isEmpty():
            self.pop()
   
