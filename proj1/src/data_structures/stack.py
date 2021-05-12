class Stack:
    def __init__(self):
        self.stack = []
        
    def size(self):
        return len(self.stack)
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, node):
        self.stack.insert(len(self.stack), node)
        
    def pop(self):
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack.pop(len(self.stack) - 1)
        
    def printQueue(self):
        print("Stack: ", end = " ")
        for i in range(len(self.stack)):
            print(self.stack[i].cost, end = " # ")
            print(self.stack[i].depth, end = " -> ")
        print("")