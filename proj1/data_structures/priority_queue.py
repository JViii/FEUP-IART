class PriorityQueue:
    def __init__(self,heuristic= "none"):
        self.queue = []
        self.heuristic=heuristic
        
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def push(self, node):
        self.queue.append(node)
        if self.heuristic=="greedy":
            self.queue = sorted(self.queue,key=lambda node : -node.heuristic)
        elif self.heuristic=="aStar":
            self.queue = sorted(self.queue,key=lambda node : node.cost+node.heuristic)
        else:
            self.queue = sorted(self.queue,key=lambda node : node.cost)
            
        
    def pop(self):
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue.pop() # last element
        
    def printQueue(self):
        print("Priority_Queue: ", end = " ")
        for i in range(len(self.queue)):
            print(self.queue[i].cost, end = " # ")
            print(self.queue[i].depth, end = " -> ")
        print("")
