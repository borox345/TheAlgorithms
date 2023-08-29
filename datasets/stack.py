"""
Stack
A linear data structure for storing one-dimensional lists.
"""
class Stack:
    def __init__(self) -> None:
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) -1]
    
    def size(self):
        return len(self.items)
    
    
stack = Stack()

stack.push("Red")
stack.push("Green")
stack.push("White")

print(stack.items)
print("----")
stack.pop()
print(stack.items)
print(stack.isEmpty())