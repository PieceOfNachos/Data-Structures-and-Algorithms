class LinkedList:
    class Node:
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev
    def __init__(self):
        self.front = None
        self.back = None
    
    def push_front(self, data):
        new_node = self.Node(data, self.front)
        if self.front is None:
            self.back = new_node
        else:
            self.front.prev = new_node
        self.front = new_node
    def pop_front(self):
        if self.front is not None:
            temp = self.front
            self.front = self.front.next
            if self.front is None:
                self.back = None
            else:
                self.front.prev = None
            del temp
    def display(self, index = 0):
        runner = self.front
        while index > 0 and runner is not None:
            runner = runner.next
            index-=1
        if runner == None: 
            print("Element with "+str(index)+" doesn't exist")
        else:
            print(runner.data)