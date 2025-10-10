from data_structures.my_array import Array

class StackStructure:
    def __init__(self, capacity):
        self.stack = Array(int, capacity)
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.stack) - 1

    def push_element(self, new_element):
        if self.is_full():
            raise Exception("Stack is full")
        self.top += 1
        self.stack[self.top] = new_element

    def pop_element(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        popped_value = self.stack[self.top]
        self.stack[self.top] = self.stack.data_type()
        self.top -= 1
        return popped_value

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[self.top]

    def size(self):
        return self.top + 1
