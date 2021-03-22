class Node:
    def __init__(self, state, parent = -1, depth = 0, cost = 0):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.cost = cost
        
        self.children = []
        self.ind = 0 # represents his number of children in reltaion to his father from left to right
        
    def setChildrenNumber(self, number):
        self.ind = number
        
    def addChildren(self, children):
        self.children.insert(len(self.children) - 1, children)

    def h(self):
        heuristic=18
        # Starting from bottom line
        for line in self.state.aquarium:
            filled = [x for x in line if x>0].length
            if(filled == self.state.rowCap()):
                heuristic-=3 # ou heuristic -=1
            else:
                break
        return heuristic