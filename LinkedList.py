class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def append(self,*value): #can append multiple values also including List. Modified to save time 
        for value in value:
            new_node = Node(value)
            if self.head is None:
                self.head = new_node
                self.tail = new_node 
                self.length = 1
            else:
                self.tail.next = new_node
                self.tail = new_node
                self.length += 1
        return True
        
    def pop(self):
        if self.length <= 0:
            return None
        else:
            temp = self.head
            prev = self.head
            while(temp.next):
                prev = temp
                temp = temp.next
            prev.next = None
            self.tail = prev
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp
            
    def prepend(self, value):
        if self.length > 0:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return True
        else:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True
            
    def popfirst(self):
        if self.length <= 1:
            return self.pop()
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        self.length -= 1 
        return temp
        
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.head
        elif index == self.length-1:
            return self.tail
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
        
    def insert(self, index, value):
        if index <0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
            return True
        if index == self.length:
            self.append(value)
            return True
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1 
        return True
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.popfirst()
        if index == self.length-1:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
        
    def reverse_LL(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True
        
        
x = LinkedList(1)
x.append(2,3,4,5,6,7,8,9,10,11,12,13,14)
x.reverse_LL()
x.print_list()
