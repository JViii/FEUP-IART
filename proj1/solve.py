from state.state import State
from data_structures.node import Node
from operators.fill import Fill
from utils.utils import *
from data_structures.priority_queue import PriorityQueue
from data_structures.myqueue import Queue
from data_structures.stack import Stack

from time import *

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#       PRINT FUNCTIONS
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# ---
# Prints the Aquarium
def printAquarium(node):
    aquarium = node.state.aquarium

    print("-----------------")
    for i in range(len(aquarium)):
        for j in range(len(aquarium)):
            print("%2d" % (aquarium[i][j]), end = " ")
        print("")

# ---
# Goes through all states and prints each one of them in order
def printSequenceOfStates(node):
    if node.parent != -1:
        printSequenceOfStates(node.parent)
    
    printAquarium(node)
        
# ---
# Prints the algorithm results
def printAlgorithmResults(algorithm, initial_time, final_node):
    elapsed_time = time() - initial_time

    if final_node == -1:
        print("There is no solution to this problem")
    else:
        printSequenceOfStates(final_node)
        
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$") 
    print("%s took: %.6f s" % (algorithm, elapsed_time))
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$") 
    
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#     AUXILIAR FUNCTIONS
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
      
# ---
# Verifies if a state is repeated
# A state can is repeated when:
#   we have already fill a cell belonging to the same aquarium in the same iteration(verification done in applyOperator)
#   we have a left cousin exatly with same aquarium cells filled
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

# ---
# Applies all the possible operators to the corresponding state
def applyOperator(node, notExpanded, allowedDepth = -1):
    aquarium = node.state.aquarium
    aquariumIndexes = [] # stores the aquarium indexes that the operator filled
    childrenNumber = 0
    
    # Verifies if we reach the max depth
    # Only used for iterative deepening search
    if node.depth == allowedDepth:
        return; 

    for i in range(len(aquarium) - 1, -1, -1):
        for j in range(len(aquarium)):
            if not abs(aquarium[i][j]) in aquariumIndexes:
                newNode = Fill(node, j, i).apply()
                if newNode != -1: # the apply operator generated a node
                    newNode.setChildrenNumber(childrenNumber) # necessary to test if it's repeated
                    if not isRepeated(newNode):
                        aquariumIndexes.append(abs(aquarium[i][j])) # adds the index of the aquarium
                        node.addChildren(newNode)
                        notExpanded.push(newNode)
                        childrenNumber += 1

# ---
# Tests if we have reached the objective state
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
            
        currNode = Node(State(copy_list(initial_node.state.aquarium), rowCap1, colCap1)) # returns to initial node
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
#          ALGORITHMS
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# Starting Node
initial_node = Node(State(copy_list(initialAquarium1), rowCap1, colCap1))

# ---
# Blind Algorithms

# bfs(initial_node) # mais ou menos 19.4s
# dfs(initial_node) # mais ou menos 0.001s
# ucs(initial_node) # mais ou menos 0.001s
# its(initial_node) # mais ou menos 16min

# ---
# Heuristic Algorithms





