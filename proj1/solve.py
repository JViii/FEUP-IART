from state import State
from node import Node
from fill import Fill
from aquarium import Aquarium
from coord import Coord
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

def isObjective(node):
    aquarium = node.state.aquarium
    rowCap = node.state.rowCap
    colCap = node.state.colCap

    # verify if each row as reached the desired capacity
    for i in range(6):
        if rowCap[i] != aquarium[i].count(1):
            return False
    
    # verify if each column as reached the desired capacity
    for i in range(6):
        cap = 0
        for j in range(6):
            cap += aquarium[j][i]
        if cap != colCap[i]:
            return False

    return True

def bfs(initial_aquarium, rowCap, colCap, aquariums):
    currNode = Node(State(copy_list(initial_aquarium), rowCap, colCap, aquariums))
    finalNode = -1

    notExpanded = [] # to change to a queue

    while True:
        if isObjective(currNode):
            finalNode = currNode
            break

        # apply operator
        applyOperator(currNode, notExpanded)

        # selects next node to process
        if len(notExpanded) == 0: # no more nodes to expand, no solution found
            break
        else:
            currNode = notExpanded.pop(len(notExpanded) - 1)

    if finalNode == -1:
        print("There is no solution to this problem")
    else:
        printSequenceOfStates(finalNode)

initialAquarium  = [[0] * 6] * 6

# one example 6x6 easy
aquariums1 = [Aquarium([Coord(0, 0), Coord(1, 0), Coord(0, 1), Coord(1, 1), Coord(2, 1), Coord(0, 2), Coord(1, 2), Coord(1, 3), Coord(2, 3), Coord(1, 4), Coord(2, 4)]),
            Aquarium([Coord(2, 0), Coord(3, 0)]),
            Aquarium([Coord(4, 0), Coord(4, 1)]),
            Aquarium([Coord(5, 0), Coord(3, 1), Coord(5, 1), Coord(2, 2), Coord(3, 2), Coord(4, 2), Coord(5, 2), Coord(5, 3), Coord(5, 4)]),
            Aquarium([Coord(0, 3), Coord(0, 4), Coord(0, 5), Coord(1, 5), Coord(2, 5)]),
            Aquarium([Coord(3, 3), Coord(4, 3), Coord(3, 4), Coord(4, 4), Coord(5, 3), Coord(5, 4), Coord(5, 5)])]
rowCap1 = [3, 5, 5, 2, 5, 5]
colCap1 = [5, 5, 4, 5, 3, 3]
