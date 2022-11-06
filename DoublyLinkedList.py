class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
        
        
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
        
    def print_DLL(self):
        temp = self.head
        while(temp):
            print(temp.value)
            temp = temp.next
          
            
    def append(self, *value):
        for value in value:
            new_node = Node(value)
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                self.length += 1
                return True
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True
    
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -=1
            return temp.value
        self.tail.prev.next = None
        self.tail.prev = None
        self.tail = temp
        self.length -= 1
        return temp.value
        
        
    def prepend(self,value):
        if self.length == 0:
            return self.append(value)
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1
        return True
        
    def popfirst(self):
        if self.length <= 1:
            return self.pop()
        temp = self.head
        self.head = temp.next
        self.head.prev  = None
        temp.next = None 
        self.length -= 1
        return temp
        
        
    def get(self, index):
        if index <0 or index >= self.length:
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        temp = self.tail
        for _ in range(self.length-1, index, -1):
            temp = temp.prev
        return temp

            
    def set(self, index, value):
        temp = self.get(index)
        if (temp):
            temp.value = value
            return True
        else:
            return False
            
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index - 1)
            new_node.next = temp.next
            new_node.prev = temp    
            temp.next.prev = new_node
            temp.next = new_node
            self.length += 1
            return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popfirst()
        if index == self.length-1:
            return self.pop()
        if self.length == 1:
            return self.pop()
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev  
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
            
x = DoublyLinkedList(1)
#x.append(2,3,4,5,6,7,8,9)
#x.prepend(0)

#x.print_DLL()
x.insert(7,100)
print("#########################")
x.remove(0)
#print(x.get(7).value)

print("#########################")
print("head = {}, tail = {}, length = {}".format(x.head.value if x.head else x.head, x.tail.value if x.tail else x.tail, x.length))
x.print_DLL()