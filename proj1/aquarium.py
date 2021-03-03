from state import State
from node import Node
from fill import Fill
from utils import *

def printAquarium(node):
    aquarium = node.state.aquarium

    print("---------------------")
    for i in range(0, 6):
        for j in range(0, 6):
            print(aquarium[i][j], end = " ")
        print("")

def printSequenceOfStates(node):
    if node.parent == -1:
        printAquarium(node)
    else:
        printSequenceOfStates(node.parent)

def applyOperator(node, notExpanded):
    # To do: avoid repeated states maybe look to the siblings
    # To generalize
    for i in range(5, -1, -1):
        for j in range(6):
            newNode = Fill(node, i, j)
            if newNode != -1: notExpanded.insert(0, newNode)

def bfs(initial_aquarium, rowCap, colCap):
    currNode = Node(State(copy_list(initial_aquarium), rowCap, colCap))
    finalNode = -1

    notExpanded = [] # to change to a queue

    while True:
        if isObjective(currNode):
            finalNode = currNode
            break

        # apply operator
        applyOperator(currNode, notExpanded)

        # selects next node to process
        if len(notExpanded) == 0:
            break
        else:
            currNode = notExpanded.pop(len(notExpanded) - 1)

    if finalNode == -1:
        print("There is no solution to this problem")
    else:
        printSequenceOfStates(finalNode)

initialAquarium  = [[0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]

rowCap = [1, 5, 2, 5, 3, 1]
colCap = [4, 3, 3, 2, 2, 3]

# initialState = State(aquarium, rowCap, colCap)
# initialNode = Node(initialState)
# newNode = Fill(initialNode, 1, 1).apply()

# printAquarium(initialNode)
# printAquarium(newNode)
