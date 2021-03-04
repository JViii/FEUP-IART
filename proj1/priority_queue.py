class PriorityQueue:
    def __init__(self):
        self.queue = []
        
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def push(self, node):
        if len(self.queue) == 0:
            self.queue.insert(0, node)
            return;
        
        j = -1
        for i in range(len(self.queue)):
            if node.cost >= self.queue[i].cost:
                j = i
                break
            
        if j == -1:
            self.queue.insert(len(self.queue), node)
        else:
            self.queue.insert(i, node)
            
        
    def pop(self):
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue.pop(len(self.queue) - 1)
        
    def printQueue(self):
        print("Priority_Queue: ", end = " ")
        for i in range(len(self.queue)):
            print(self.queue[i].cost, end = " # ")
            print(self.queue[i].depth, end = " -> ")
        print("")