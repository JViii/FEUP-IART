class Queue:
    def __init__(self):
        self.queue = []
        
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def push(self, node):
        self.queue.insert(len(self.queue), node)
            
    def pop(self):
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue.pop(0)
        
    def printQueue(self):
        print("Queue: ", end = " ")
        for i in range(len(self.queue)):
            print(self.queue[i].cost, end = " # ")
            print(self.queue[i].depth, end = " -> ")
        print("")