class Node:
    def __init__(self, state, parent = -1, depth = 0, cost = 0):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.cost = cost
        self.impossibleAquariums = []
        self.heuristic= self.lineMoves()
        self.exp = self.heuristic
        # print(self.impossibleAquariums)
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

    # ---
    # DIFFERENT HEURISTIC

    def lineMoves(self):
        aquarium = self.state.aquarium
        heuristic = 0

        linesBellow = []
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

            nm = self.numMoves(cells, self.state.rowCap[line], line, linesBellow)
            # print(cells, self.state.rowCap[line], nm)
            heuristic += nm
            linesBellow.insert(0, dict(cells))

        # print( "---------------")

        return heuristic

    def possibleAquarium(self, cells, line, aq, linesBellow):
        aquarium = self.state.aquarium
        colCap = self.state.colCap
        rowCap = self.state.rowCap

        max = -1

        for j in range(len(aquarium)):
            counterFill = 0
            counterEmpty = 0
            
            for i in range(len(aquarium)):
                if aquarium[i][j] > 0: counterFill += 1
                if line < i and aquarium[i][j] < 0 and abs(aquarium[i][j]) == aq: 
                    counterEmpty += 1 
                    if (linesBellow[i - line - 1].get(aq)[1] + self.getNumFilledCellsInRow(linesBellow[i - line - 1])) > rowCap[i]: 
                        # print((self.getNumFilledCellsInRow(linesBellow[i - line - 1])), aq, line, i)
                        return -1
            
            if (counterEmpty + counterFill) > colCap[j]: return -1
            if max < counterEmpty: max = counterEmpty

        return max

    def getNumFilledCellsInRow(self, cells):
        numFill = 0

        for aq in cells:
            numFill += cells.get(aq)[0]

        return numFill

    def numMoves(self, cells, cap, line, linesBellow):
        # quantas celulas estao cheias na linha
        numFill = self.getNumFilledCellsInRow(cells)

        # linha ja esta cheia
        if (cap-numFill) == 0: return 0

        # já não é possivel chagar a uma solucao
        min = self.selectMinAquariumEmpty(cells)
        if cells.get(min)[1] > (cap - numFill):  return 1000

        min = 100000000
        imp = []
        for aq in cells:

            if cells.get(aq)[1] != 0:
                cells1 = dict(cells)
                cells1[aq] = [cells.get(aq)[1], 0]
                # print("Id: %s -> Result: %s" % (aq, self.possibleAquarium(cells1, line, aq)))
                moves = self.possibleAquarium(cells1, line, aq, linesBellow)
                # print(aq, moves)
                if moves != -1: 
                    val = moves + 1 + self.numMoves(cells1, cap, line, linesBellow)
                    if val < min: min = val
                    if val >= 1000: imp.append(aq)
                else: imp.append(aq)
        
        self.impossibleAquariums = list(imp)

        return min
        
    def selectMinAquariumEmpty(self, cells):
        min = len(self.state.aquarium) + 1
        id = -1
        
        for aq in cells:
            if cells.get(aq)[1] != 0 and cells.get(aq)[1] < min:
                min = cells.get(aq)[1]
                id = aq

        return id