from data_structures.node import Node
from state.state import State
from utils.utils import copy_list

class Fill:
    def __init__(self, node, aquariumID):
        self.node = node
        self.aquarium = node.state.aquarium
        self.rowCap = node.state.rowCap
        self.colCap = node.state.colCap
        self.aquariumID = aquariumID
    
    def getFullElemInCol(self, x):
        col = []
        for i in range(len(self.aquarium)):
            if self.aquarium[i][x] > 0:
                col.append(self.aquarium[i][x])
            
        return col
    
    def getFullElemInRow(self, y):
        return [l for l in self.aquarium[y] if l > 0]
    
    def getCellsToFill(self):
        #line = self.aquarium[self.y]
        aquarium = [] # [[x1,y1],[x2,y2]...]
        cells = []

        # Optimizations class with following attributes:
        # CurrentWaterLevel - ultima linha que foi preenchida (-1 se está vazio)
        # Max water level - linha mais a cima do aquario

        for line in range(len(self.aquarium) - 1, -1, -1):
          for col in range(len(self.aquarium)):
            if self.aquarium[line][col] == -self.aquariumID: # only unfilled cells
              aquarium.append([line,col])

        if(aquarium != []):
          maxval = max(aquarium,key=lambda x: x[0] )[0]
          cells = [[y,x] for [y,x] in aquarium if y==maxval]

        return cells

    
    def canFillCol(self, cells):
        # Makes sure column cap isn't exceeded
        for cell in cells:
            col = self.getFullElemInCol(cell[1])
            if len(col) + 1 > self.colCap[cell[1]]:
                return False
            
        return True
    
    def canFillRow(self, cells):
        # Makes sure row cap isn't exceeded
        return len(self.getFullElemInRow(cells[0][0])) + len(cells) <= self.rowCap[cells[0][0]] #cells[0][0]=y

    # Verifies if we can apply the operator
    def preconditions(self, cells):
        return (self.canFillRow(cells)) and (self.canFillCol(cells)) # capacities not exceded
      
    def fillCells(self, cells):
        newAquarium = copy_list(self.node.state.aquarium)

        for [y,x] in cells:
            newAquarium[y][x] = self.aquariumID
            
        return newAquarium

    def apply(self):
        cells = self.getCellsToFill()
        # print(cells)
        
        if len(cells) == 0 or not self.preconditions(cells): return -1

        return Node(State(self.fillCells(cells), self.node.state.rowCap, self.node.state.colCap), self.node, self.node.depth + 1, self.node.cost + len(cells))
