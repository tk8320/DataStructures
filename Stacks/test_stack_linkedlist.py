import pytest
from stack_using_linkedlist import Stack
from stack_using_list import Stack as Stack_list

class TestStackLinkedList:
    ll = Stack()
    def test_push(self):
        curr_len = self.ll.len
        self.ll.push(10)
        assert self.ll.len == curr_len + 1
        assert self.ll.pop() == 10

    def test_pop(self):
        self.ll.push(10)
        curr_len = self.ll.len
        assert self.ll.pop() == 10
        assert self.ll.len == curr_len - 1

    def test_isEmpty(self):
        assert self.ll.isEmpty() == True
        self.ll.push(10)
        assert self.ll.isEmpty() == False
        self.ll.pop()

    def test_truncate(self):
        self.ll.push(10)
        self.ll.push(20)
        curr_len = self.ll.len
        self.ll.truncate()
        assert self.ll.len == 0


class TestStackList:
    ll = Stack_list()
    def test_push(self):
        curr_len = self.ll.len
        self.ll.push(10)
        assert self.ll.len == curr_len + 1
        assert self.ll.pop() == 10

    def test_pop(self):
        self.ll.push(10)
        curr_len = self.ll.len
        assert self.ll.pop() == 10
        assert self.ll.len == curr_len - 1

    def test_isEmpty(self):
        assert self.ll.isEmpty() == True
        self.ll.push(10)
        assert self.ll.isEmpty() == False
        self.ll.pop()

    def test_truncate(self):
        self.ll.push(10)
        self.ll.push(20)
        curr_len = self.ll.len
        self.ll.truncate()
        assert self.ll.len == 0
         