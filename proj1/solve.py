from state import State
from node import Node
from fill import Fill
from aquarium import Aquarium
from cell import Cell
from utils import copy_list
from priority_queue import PriorityQueue
from myqueue import Queue
from stack import Stack

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
            if newNode != -1: notExpanded.push(newNode)

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

    notExpanded = Queue()

    while True:
        if isObjective(currNode):
            finalNode = currNode
            break

        # apply operator
        applyOperator(currNode, notExpanded)

        # selects next node to process
        if notExpanded.isEmpty(): # no more nodes to expand, no solution found
            break
        else:
            currNode = notExpanded.pop()

    if finalNode == -1:
        print("There is no solution to this problem")
    else:
        printSequenceOfStates(finalNode)

initialAquarium  = [[0] * 6] * 6

# one example 6x6 easy
aquariums1 = [Aquarium([Cell(0, 0), Cell(1, 0), Cell(0, 1), Cell(1, 1), Cell(2, 1), Cell(0, 2), Cell(1, 2), Cell(1, 3), Cell(2, 3), Cell(1, 4), Cell(2, 4)]),
            Aquarium([Cell(2, 0), Cell(3, 0)]),
            Aquarium([Cell(4, 0), Cell(4, 1)]),
            Aquarium([Cell(5, 0), Cell(3, 1), Cell(5, 1), Cell(2, 2), Cell(3, 2), Cell(4, 2), Cell(5, 2), Cell(5, 3), Cell(5, 4)]),
            Aquarium([Cell(0, 3), Cell(0, 4), Cell(0, 5), Cell(1, 5), Cell(2, 5)]),
            Aquarium([Cell(3, 3), Cell(4, 3), Cell(3, 4), Cell(4, 4), Cell(5, 3), Cell(5, 4), Cell(5, 5)])]
rowCap1 = [3, 5, 5, 2, 5, 5]
colCap1 = [5, 5, 4, 5, 3, 3]


# -------------------------------
# IDEA FOR STATE
# -------------------------------

#rowCap, colCap igual ao que se tem

# isto representaria o aquario inicial
# valores com o mesmo valor absoluto pertencem ao mesmo aquario
# valores negativos significa que a celula esta vazia
# valores positivos significa que a celula esta cheia

# [[-1, -1, -1, -2, -2, -2],
#  [-1, -3, -3, -2, -2, -4],
#  [-1, -3, -3, -2, -2, -4],
#  [-3, -3, -4, -4, -4, -4],
#  [-3, -3, -3, -4, -5, -4],
#  [-3, -3, -6, -6, -5, -4]]


