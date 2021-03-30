class Node:
    def __init__(self, state, parent = -1, depth = 0, cost = 0):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.cost = cost
        self.heuristic= self.hRow()
        self.lineMoves()
        
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
        #return (self.hCol()+self.hRow()) 
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
        empty = 0
        full = 0
        listMoves = []

        aquarium = self.state.aquarium
        
        for line in range(len(aquarium) - 1, -1, -1):
            listMoves1 = {}
            for col in range(len(aquarium)):
                numCheios = 0
                numVazios = 0
                
                if abs(aquarium[line][col]) in listMoves1:
                    numCheios = listMoves1.get(abs(aquarium[line][col]))[0]
                    numVazios = listMoves1.get(abs(aquarium[line][col]))[1]
                
                if aquarium[line][col] > 0: numCheios += 1
                else: numVazios += 1
                listMoves1[abs(aquarium[line][col])] = [numCheios, numVazios]
                
            listMoves.append(listMoves1)

        # falta implementar o resto da heuristica

        print(listMoves)