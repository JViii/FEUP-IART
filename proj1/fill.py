from node import Node
from state import State
from utils import *

class Fill:
    def __init__(self, node, cell):
        self.node = node
        self.cell = cell

    # def exceedRowCap():

    # def exceedColCap():

    # def canFill(aquario,cell):
    #     # the cell is laready filled
    #     if(board[cell.y][cell.x] == 1):
    #         return false

    #     line = board[cell.y]
    #     col = board[cell.x]

    #     if(line.count(1) < maxWaterPerLine[cell.y] and col.count(1) < maxWaterPerCol[cell.x]):
    #         return noAirBelow(cell)
    #     else:
    #         return false

    # Verifies if we can apply the operator
    def preconditions(self):
        return True

    def apply(self):
        if not self.preconditions(): return -1

        newAquarium = copy_list(self.node.state.aquarium)
        newAquarium[self.x][self.y] = 1
        return Node(State(newAquarium, self.node.state.rowCap, self.node.state.colCap), self.node)
        #return -1 # the operator was not applied
