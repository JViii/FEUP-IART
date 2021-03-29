from data_structures.node import Node
from state.state import State
from utils.utils import copy_list

class FillHuman:
    def __init__(self, node, aquariumID):
        self.node = node
        self.aquarium = node.state.aquarium
        self.rowCap = node.state.rowCap
        self.colCap = node.state.colCap
        self.aquariumID = aquariumID
    
    def getCellsToFill(self):
        cells = [] # [[x1,y1],[x2,y2]...]

        # Optimizations class with following attributes:
        # CurrentWaterLevel - ultima linha que foi preenchida (-1 se está vazio)
        # Max water level - linha mais a cima do aquario

        for line in range(len(self.aquarium) - 1, -1, -1):
            for col in range(len(self.aquarium)):
                if self.aquarium[line][col] == -self.aquariumID: # only unfilled cells
                    cells.append([line,col])
            if len(cells) != 0: return cells

        return cells
      
    def fillCells(self, cells):
        newAquarium = copy_list(self.node.state.aquarium)

        for [y,x] in cells:
            newAquarium[y][x] = self.aquariumID
            
        return newAquarium

    def apply(self):
        cells = self.getCellsToFill()

        if len(cells) == 0: return -1

        return Node(State(self.fillCells(cells), self.node.state.rowCap, self.node.state.colCap), self.node, self.node.depth + 1, self.node.cost + len(cells))
