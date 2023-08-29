"""
Que
Stores n elemnts in one-dimensional structur.
"""

class Queue:
    def __init__(self) -> None:
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)
    

queue = Queue()

queue.enqueue('Red')
queue.enqueue('White')
queue.enqueue('Pink')

print(queue.size())
print(queue.items)
print("----")

queue.dequeue()
print(queue.items)
print(queue.size())