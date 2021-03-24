from data_structures.node import Node
from state.state import State
from utils.utils import copy_list

class Unfill:
    def __init__(self, node, aquariumID):
        self.node = node
        self.aquarium = node.state.aquarium
        self.aquariumID = aquariumID
    
    def getCellsToUnfill(self):
        cells = []

        # Optimizations class with following attributes:
        # CurrentWaterLevel - ultima linha que foi preenchida (-1 se está vazio)
        # Max water level - linha mais a cima do aquario

        for line in range(len(self.aquarium)):
          for col in range(len(self.aquarium)):
            if self.aquarium[line][col] == -self.aquariumID: # only filled cells
              cells.append([line,col])
          if len(cells) != 0: return cells
              

        return cells

    def unfillCells(self, cells):
        newAquarium = copy_list(self.node.state.aquarium)

        for [y,x] in cells:
            newAquarium[y][x] = self.aquariumID
            
        return newAquarium

    def apply(self):
        cells = self.getCellsToUnfill()
        
        if len(cells) == 0: return -1

        return Node(State(self.unfillCells(cells), self.node.state.rowCap, self.node.state.colCap), self.node.parent.parent, self.node.depth - 1, self.node.cost - len(cells))
