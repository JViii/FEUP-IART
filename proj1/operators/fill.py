from data_structures.node import Node
from state.state import State
from utils.utils import copy_list

class Fill:
    def __init__(self, node, x, y):
        self.node = node
        self.aquarium = node.state.aquarium
        self.rowCap = node.state.rowCap
        self.colCap = node.state.colCap
        self.x = x
        self.y = y
    
    def getFullElemInCol(self, x):
        col = []
        for i in range(len(self.aquarium)):
            if self.aquarium[i][x] > 0:
                col.append(self.aquarium[i][x])
            
        return col
    
    def getFullElemInRow(self):
        return [l for l in self.aquarium[self.y] if l > 0]
    
    def noAirBelow(self, cells):
        if self.y == len(self.aquarium) - 1: 
            return True
        
        id = abs(self.aquarium[self.y][self.x])
        for x in cells:
            val = self.aquarium[self.y + 1][x]
            if abs(val) == id and val < 0:
                return False
            
        return True
    
    def getSameAquariumXs(self):
        line = self.aquarium[self.y]
        id = abs(line[self.x])
        ret = []
        
        for i in range(len(line)):
            if id == abs(line[i]) and line[i] < 0:
                ret.append(i)
                
        return ret
    
    def canFillCol(self, cells):
        # Makes sure column cap isn't exceeded
        for i in cells:
            col = self.getFullElemInCol(i)
            if len(col) + 1 > self.colCap[i]:
                return False
            
        return True
    
    def canFillRow(self, cells):
        # Makes sure row cap isn't exceeded
        return len(self.getFullElemInRow()) + len(cells) <= self.rowCap[self.y]

    # Verifies if we can apply the operator
    def preconditions(self, cells):
        if (self.canFillRow(cells)) and (self.canFillCol(cells)): # capacities not exceded
            return self.noAirBelow(cells)
        else:
          return False
      
    def fillCells(self, cells):
        newAquarium = copy_list(self.node.state.aquarium)

        for i in cells:
            newAquarium[self.y][i] = abs(newAquarium[self.y][i])
            
        return newAquarium

    def apply(self):
        cells = self.getSameAquariumXs()
        # print(cells)
        
        if len(cells) == 0 or not self.preconditions(cells): return -1

        return Node(State(self.fillCells(cells), self.node.state.rowCap, self.node.state.colCap), self.node, self.node.depth + 1, self.node.cost + len(cells))
