from state.state import State
from data_structures.node import Node
from operators.fill import Fill
from utils.utils import *
from data_structures.priority_queue import PriorityQueue
from data_structures.myqueue import Queue
from data_structures.stack import Stack

from time import *

def printAquarium(node):
    aquarium = node.state.aquarium

    print("-----------------")
    for i in range(len(aquarium)):
        for j in range(len(aquarium)):
            print("%2d" % (aquarium[i][j]), end = " ")
        print("")

def printSequenceOfStates(node):
    if node.parent == -1:
        printAquarium(node)
    else:
        printSequenceOfStates(node.parent)
        printAquarium(node)
        
def printAlgorithmResults(algorithm, initial_time, final_node):
    elapsed_time = time() - initial_time

    if final_node == -1:
        print("There is no solution to this problem")
    else:
        printSequenceOfStates(final_node)
        
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$") 
    print("%s took: %.6f s" % (algorithm, elapsed_time))
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$") 
        
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

def applyOperator(node, notExpanded, allowedDepth = -1):
    # To do: avoid repeated states maybe look to the siblings
    aquarium = node.state.aquarium
    aux = []
    childrenNumber = 0
    
    # Verifies if we reach the max depth
    # Only used for iterative deepening search
    if node.depth == allowedDepth:
        return; 

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

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#           ALGORITHMS
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# ---
# Breadth First Search
def bfs(initial_node):
    currNode = initial_node
    finalNode = -1

    notExpanded = Queue()

    start = time()
    
    print("Solving using BFS...")

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
    
    printAlgorithmResults("BFS", start, finalNode)
        
# ---    
# Depth First Search        
def dfs(initial_node):
    currNode = initial_node
    finalNode = -1

    notExpanded = Stack()

    start = time()
    
    print("\nSolving using DFS...")

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
        
    printAlgorithmResults("DFS", start, finalNode)

# ---
# Uniform Cost Search
def ucs(initial_node):
    currNode = initial_node
    finalNode = -1

    notExpanded = PriorityQueue();

    start = time();
    
    print("\nSolving using UCS...")

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
    
    printAlgorithmResults("UCS", start, finalNode) 
    
# ---
# Iterative Deepening Search
def its(initial_node):
    currNode = initial_node
    finalNode = -1

    notExpanded = Stack();
    depth = 0

    start = time();
    
    print("\nSolving using ITS...")

    while True:
        
        print("Depth: %d" % (depth))
        
        while True:
            if isObjective(currNode):
                finalNode = currNode
                break
    
            # apply operator
            applyOperator(currNode, notExpanded, depth)
    
            # selects next node to process
            if notExpanded.isEmpty(): # no more nodes to expand, no solution found
                break
            else:
                currNode = notExpanded.pop()
                
        if finalNode != -1:
            break;
            
        currNode = initial_node # returns to initial node
        depth += 1 # increases its depth
    
    printAlgorithmResults("ITS", start, finalNode)
    
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#       AQUARIUM EXAMPLES
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# ---
# Ex1
initialAquarium1 = [[-1, -1, -1, -2, -2, -2],
                    [-1, -3, -3, -2, -2, -4],
                    [-1, -3, -3, -2, -2, -4],
                    [-3, -3, -4, -4, -4, -4],
                    [-3, -3, -3, -4, -5, -4],
                    [-3, -3, -6, -6, -5, -4]]

rowCap1 = [3, 5, 5, 2, 5, 5]
colCap1 = [5, 5, 4, 5, 3, 3]

# ---
# Ex2
initialAquarium2 = [[-1,-5,-5,-6,-6,-6],
                    [-1,-5,-5,-6,-5,-5],
                    [-1,-1,-5,-5,-5,-5],
                    [-2,-1,-1,-3,-4,-5],
                    [-2,-2,-1,-3,-4,-5],
                    [-3,-3,-3,-3,-3,-5]]

rowCap2 = [3,2,2,4,5,5]
colCap2 = [5,4,3,4,4,1]

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#       BLIND ALGORITHMS
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# Starting Node
initial_node = Node(State(copy_list(initialAquarium1), rowCap1, colCap1))

# bfs(initial_node)
# dfs(initial_node)
# ucs(initial_node)
its(initial_node)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#       HEURISTIC ALGORITHMS
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$



