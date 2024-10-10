class LinkedList:
    class Node:
        def __init__(self, data, next = None, prev = None):
            self.data = data
            self.next = next
            self.prev = prev
    def __init__(self):
        self.front = self.Node(None)
        self.back = self.Node(None, None, self.front)
        self.front.next = self.back
    def push_front(self,data):
        new_node = self.Node(data, self.front.next, self.front)
        self.front.next.prev = new_node
        self.front.next = new_node
    def pop_front(self):
        temp = self.front.next
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        del temp
    def display(self, index = 0):
        runner = self.front.next
        while index > 0 and runner is not None:
            runner = runner.next
            index-=1
        if runner == None: 
            print("Element with "+str(index)+" doesn't exist")
        else:
            print(runner.data)