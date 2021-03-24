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
        for line in range(len(self.state.aquarium) - 1, -1, -1):
            filled=len([x for x in self.state.aquarium[line] if x>0])
            if(filled == self.state.rowCap[line]):
                heuristic-=3 # ou heuristic -=1
            else:
                break

        return heuristic