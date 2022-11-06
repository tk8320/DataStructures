

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.head = None
        self.len = 0

    def isEmpty(self) -> bool:
        if self.len == 0:
            return True
        else:
            return False
    

    def push(self, data) -> None:
        node = Node(data)
        if self.len == 0:
            self.head = node
        else:
            node.next = self.head
            self.head = node 
        self.len += 1

    def pop(self):
        if self.len == 0 :
            return -1
        elif self.len == 1:
            data = self.head.data
            self.head =None
            self.len -= 1
            return data
        else:
            data = self.head.data
            self.head = self.head.next
            self.len -= 1
            return data

    def truncate(self):
        while not self.isEmpty():
            self.pop()

