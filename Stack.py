class Stack:
    def __init__(self):
        self.index = []
    def len(self):
        return len(self.index)
    def push(self, data):
        self.index.insert(0,data)
    def peek(self):
        if len(self) == 0:
            raise Exception("Peek was called on empty stack")
        return self.index[0]
    def pop(self):
        if len(self) == 0:
            raise Exception("pop() called on empty stack.")
        return self.__index.pop(0)
    def __str__(self):
        return str(self.__index)