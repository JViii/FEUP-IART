from state import State
from node import Node
from fill import Fill

def printAquarium(node):
    aquarium = node.state.aquarium

    print("---------------------")
    for i in range(0, 6):
        for j in range(0, 6):
            print(aquarium[i][j], end = " ")
        print("")


aquarium  = [[0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]

rowCap = [1, 5, 2, 5, 3, 1]
colCap = [4, 3, 3, 2, 2, 3]

initialState = State(aquarium, rowCap, colCap)
initialNode = Node(initialState)
newNode = Fill(initialNode, 1, 1).apply()

printAquarium(initialNode)
printAquarium(newNode)
