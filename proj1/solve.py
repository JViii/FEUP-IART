from state import State
from node import Node
from fill import Fill
from utils import *
from priority_queue import PriorityQueue
from myqueue import Queue
from stack import Stack

from time import *

def printAquarium(node):
    aquarium = node.state.aquarium

    print("---------------------")
    for i in range(len(aquarium)):
        for j in range(len(aquarium)):
            print(aquarium[i][j], end = " ")
        print("")

def printSequenceOfStates(node):
    if node.parent == -1:
        printAquarium(node)
    else:
        printSequenceOfStates(node.parent)
        printAquarium(node)
        
def isRepeated(node):
    grandparent = node.parent.parent
    parentIndex = node.parent.ind
    
    if grandparent == -1:
        return False # it has no grandparent
    
    leftChildren = [l for l in grandparent.children if l.ind < parentIndex]
    
    for i in leftChildren:
        cousins = i.children
        for j in cousins:
            if compare_lists(j.state.aquarium, node.state.aquarium):
                return True
            
    return False

def applyOperator(node, notExpanded):
    # To do: avoid repeated states maybe look to the siblings
    aquarium = node.state.aquarium
    aux = []
    childrenNumber = 0

    for i in range(len(aquarium) - 1, -1, -1):
        for j in range(len(aquarium)):
            if not abs(aquarium[i][j]) in aux:
                newNode = Fill(node, j, i).apply()
                if newNode != -1:
                    newNode.setChildrenNumber(childrenNumber)
                    if not isRepeated(newNode):
                        aux.append(abs(aquarium[i][j]))
                        node.addChildren(newNode)
                        notExpanded.push(newNode)
                        childrenNumber += 1

def isObjective(node):
    aquarium = node.state.aquarium
    rowCap = node.state.rowCap
    colCap = node.state.colCap

    # verify if each row as reached the desired capacity
    for i in range(len(aquarium)):
        usedCap = len([l for l in aquarium[i] if l > 0])
        if rowCap[i] != usedCap:
            return False
    
    # verify if each column as reached the desired capacity
    for i in range(len(aquarium)):
        cap = 0
        for j in range(len(aquarium)):
            if aquarium[j][i] > 0:
                cap += 1
        if cap != colCap[i]:
            return False

    return True

def bfs(initial_aquarium, rowCap, colCap):
    currNode = Node(State(copy_list(initial_aquarium), rowCap, colCap))
    finalNode = -1

    notExpanded = Queue()

    start = time()

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
    
    elapsed_time = time() - start

    if finalNode == -1:
        print("There is no solution to this problem")
    else:
        printSequenceOfStates(finalNode)
        
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$") 
    print("BFS took: ", elapsed_time, "s")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$") 
        
        
def dfs(initial_aquarium, rowCap, colCap):
    currNode = Node(State(copy_list(initial_aquarium), rowCap, colCap))
    finalNode = -1

    notExpanded = Stack()

    start = time()

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
        
    elapsed_time = time() - start

    if finalNode == -1:
        print("There is no solution to this problem")
    else:
        printSequenceOfStates(finalNode)
        
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$") 
    print("DFS took: ", elapsed_time, "s")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$") 

def ucs(initial_aquarium, rowCap, colCap):
    currNode = Node(State(copy_list(initial_aquarium), rowCap, colCap))
    finalNode = -1

    notExpanded = PriorityQueue();

    start = time();

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
    
    elapsed_time = time() - start

    if finalNode == -1:
        print("There is no solution to this problem")
    else:
        printSequenceOfStates(finalNode)
        
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$") 
    print("UCS took: ", elapsed_time, "s")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$") 

# one example 6x6 easy
initialAquarium1 = [[-1, -1, -1, -2, -2, -2],
                  [-1, -3, -3, -2, -2, -4],
                  [-1, -3, -3, -2, -2, -4],
                  [-3, -3, -4, -4, -4, -4],
                  [-3, -3, -3, -4, -5, -4],
                  [-3, -3, -6, -6, -5, -4]]
rowCap1 = [3, 5, 5, 2, 5, 5]
colCap1 = [5, 5, 4, 5, 3, 3]

initialAquarium2 = [[-2, -1, -1],
                  [-1, -1, -1],
                  [-1, -1, -1]]
rowCap2 = [2, 3, 3]
colCap2 = [2, 3, 3]

aq = [[-1,-5,-5,-6,-6,-6],
      [-1,-5,-5,-6,-5,-5],
      [-1,-1,-5,-5,-5,-5],
      [-2,-1,-1,-3,-4,-5],
      [-2,-2,-1,-3,-4,-5],
      [-3,-3,-3,-3,-3,-5]]

rowc = [3,2,2,4,5,5]
colc = [5,4,3,4,4,1]

#dfs(initialAquarium1, rowCap1, colCap1)
#bfs(initialAquarium1, rowCap1, colCap1)
ucs(initialAquarium1, rowCap1, colCap1)



