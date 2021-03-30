class Node:
    def __init__(self, state, parent = -1, depth = 0, cost = 0):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.cost = cost
        self.heuristic= self.lineMoves()
        self.exp = self.heuristic
        
        self.children = []
        self.ind = 0 # represents his number of children in reltaion to his father from left to right
        
    def setChildrenNumber(self, number):
        self.ind = number
        
    def addChildren(self, children):
        self.children.insert(len(self.children) - 1, children)

    def hRow(self):
        heuristic=len(self.state.aquarium)
        #h=0;
        # Starting from bottom line
        for line in range(len(self.state.aquarium) - 1, -1, -1):
            filled=len([x for x in self.state.aquarium[line] if x>0])
           # h+=(self.state.rowCap[line]-filled)
            if(filled == self.state.rowCap[line]):
                heuristic-=1
          

        return heuristic

    def hCol(self):
        heuristic=len(self.state.aquarium)
        column = []
        h=0

        # Starting from bottom line
        for col in range(len(self.state.aquarium)):
            for line in range(len(self.state.aquarium)):
                if self.state.aquarium[line][col] > 0:
                    column.append(self.state.aquarium[line][col])
            #h+=(self.state.rowCap[line]-len(column))
            if(len(column) == self.state.colCap[col]):
                heuristic-=1
            column = []

        return heuristic

    def hRowCol(self):
        heuristic=len(self.state.aquarium)
        column = []

        # Starting from bottom line
        for x in range(len(self.state.aquarium)):
            filled=len([l for l in self.state.aquarium[x] if l>0]) #linha

            for y in range(len(self.state.aquarium)): #coluna
                if self.state.aquarium[y][x] > 0:
                    column.append(self.state.aquarium[y][x]) 

            if(len(column) == self.state.colCap[x]):
                heuristic-=1
            if(filled == self.state.rowCap[y]):
                heuristic-=1
            column = []

        return heuristic

    def lineMoves(self):
        aquarium = self.state.aquarium
        heuristic = 0

        for line in range(len(aquarium) - 1, -1, -1):
            cells = {}
            for col in range(len(aquarium)):
                numCheios = 0
                numVazios = 0
                
                if abs(aquarium[line][col]) in cells:
                    numCheios = cells.get(abs(aquarium[line][col]))[0]
                    numVazios = cells.get(abs(aquarium[line][col]))[1]
                
                if aquarium[line][col] > 0: numCheios += 1
                else: numVazios += 1
                cells[abs(aquarium[line][col])] = [numCheios, numVazios]

            heuristic += self.numMoves(cells, self.state.rowCap[line])

        return heuristic

    def numMoves(self, cells, cap):
        numFill = 0
        for aq in cells:
            numFill += cells.get(aq)[0]

        if (cap-numFill) == 0: return 0

        min = self.selectMinAquariumEmpty(cells)
        if cells.get(min)[1] > (cap - numFill):  return 1000

        min = 100000000
        for aq in cells:
            if cells.get(aq)[1] != 0:
                cells1 = dict(cells)
                cells1[aq] = [cells.get(aq)[1], 0]
                val = 1 + self.numMoves(cells1, cap)
                if val < min: min = val

        return min
        
    def selectMinAquariumEmpty(self, cells):
        min = len(self.state.aquarium) + 1
        id = -1
        
        for aq in cells:
            if cells.get(aq)[1] != 0 and cells.get(aq)[1] < min:
                min = cells.get(aq)[1]
                id = aq

        return id