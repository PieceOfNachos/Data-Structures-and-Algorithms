class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, data):
        self.items.insert(0,data)
    def dequeue(self):
        self.items.pop()
    def size(self):
        return len(self.items)
    def peek(self):
        print(self.items)
