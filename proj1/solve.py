from state.state import State
from data_structures.node import Node
from operators.fill import Fill
from operators.unfill import Unfill
from utils.utils import *
from data_structures.priority_queue import PriorityQueue
from data_structures.myqueue import Queue
from data_structures.stack import Stack

from time import *

import numbers

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
#   we have cousins exatly with same aquarium cells filled
def isRepeated(node):
    grandparent = node.parent.parent
    parentIndex = node.parent.ind
    
    if grandparent == -1:
        return False # it has no grandparent
    
    children = [l for l in grandparent.children if l.ind != parentIndex]
    
    for i in children:
        cousins = i.children
        for j in cousins:
            if compare_lists(j.state.aquarium, node.state.aquarium):
                return True
            
    return False

# ---
# Applies all the possible operators to the corresponding state
def applyOperator(node, notExpanded, nAquariums, allowedDepth = -1):
    aquarium = node.state.aquarium
    childrenNumber = 0
    
    # Verifies if we reach the max depth
    # Only used for iterative deepening search
    if node.depth == allowedDepth:
        return; 

    for i in range(1,nAquariums+1):
      newNode = Fill(node, i).apply()
      if newNode != -1:
        newNode.setChildrenNumber(childrenNumber) # necessary to test if it's repeated
        if not isRepeated(newNode):
          node.addChildren(newNode)
          notExpanded.push(newNode)
          childrenNumber += 1

   
# ---
# Counts how many cells are filled in row
def numCellsFilledInRow(aquarium, row):
    return len([l for l in aquarium[row] if l > 0])

# ---
# Counts how many cells are filled in col
def numCellsFilledInCol(aquarium, col):
    ret = 0
    for i in range(len(aquarium)):
            if aquarium[i][col] > 0:
                ret += 1
    return ret

# ---
# Tests if we have reached the objective state
def isObjective(node):
    aquarium = node.state.aquarium
    rowCap = node.state.rowCap
    colCap = node.state.colCap

    # verify if each row as reached the desired capacity
    for i in range(len(aquarium)):
        if rowCap[i] != numCellsFilledInRow(aquarium, i) or colCap[i] != numCellsFilledInCol(aquarium, i):
                return False

    return True

# ---
# Evaluates the current state
# The lesser is the value the closer we are from a solution
def evaluate(node):
    aquarium = node.state.aquarium
    rowCap = node.state.rowCap
    colCap = node.state.colCap
    
    val = 0
    
    # goes through all rows and colls and counts how many cells we need to fill
    # to complete the aquarium
    for i in range(len(aquarium)):
        val += rowCap[i] - numCellsFilledInRow(aquarium, i)
        val += colCap[i] - numCellsFilledInCol(aquarium, i)
        
    return val

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#           ALGORITHMS
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# ---
# Breadth First Search
def bfs(initial_node):
    currNode = initial_node
    finalNode = -1
    
    nAquariums = max([abs(x) for x in set(sum(initial_node.state.aquarium,[]))]) #Number of aquariums

    notExpanded = Queue()

    start = time()
    
    print("\nSolving using BFS...")

    while True:
        if isObjective(currNode):
            finalNode = currNode
            break

        # apply operator
        applyOperator(currNode, notExpanded, nAquariums)

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

    nAquariums = max([abs(x) for x in set(sum(initial_node.state.aquarium,[]))]) #Number of aquariums

    notExpanded = Stack()

    start = time()
    
    print("\nSolving using DFS...")

    while True:
        if isObjective(currNode):
            finalNode = currNode
            break

        # apply operator
        applyOperator(currNode, notExpanded, nAquariums)

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

    nAquariums = max([abs(x) for x in set(sum(initial_node.state.aquarium,[]))]) #Number of aquariums

    notExpanded = PriorityQueue();

    start = time();
    
    print("\nSolving using UCS...")

    while True:
        if isObjective(currNode):
            finalNode = currNode
            break

        # apply operator
        applyOperator(currNode, notExpanded, nAquariums)

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

    nAquariums = max([abs(x) for x in set(sum(initial_node.state.aquarium,[]))]) #Number of aquariums
    notExpanded = Stack();
    depth = 0

    start = time();
    
    print("\nSolving using ITS...")

    while True:
        while True:
            if isObjective(currNode):
                finalNode = currNode
                break
    
            # apply operator
            applyOperator(currNode, notExpanded, nAquariums, depth)
    
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


# ---
# Greedy Search
def greedy(initial_node):
    currNode = initial_node
    finalNode = -1

    nAquariums = max([abs(x) for x in set(sum(initial_node.state.aquarium,[]))]) #Number of aquariums

    notExpanded = PriorityQueue("greedy")

    start = time()
    print("\nSolving using Greedy Search...")

    while True:
        if isObjective(currNode):
            finalNode = currNode
            break

        #printAquarium(currNode)
        #print(currNode.heuristic)
        #sleep(1)
        #change cost
#        currNode.cost=currNode.hRow()

        # apply operator
        applyOperator(currNode, notExpanded,nAquariums)

        # selects next node to process
        if notExpanded.isEmpty(): # no more nodes to expand, no solution found
            break
        else:
            currNode = notExpanded.pop()
    
    printAlgorithmResults("Greedy", start, finalNode)    
    


# ---
# A* 
def aStar(initial_node):
    currNode = initial_node
    finalNode = -1

    nAquariums = max([abs(x) for x in set(sum(initial_node.state.aquarium,[]))]) #Number of aquariums

    notExpanded = PriorityQueue("aStar")

    start = time()
    print("\nSolving using A*...")

    while True:
        if isObjective(currNode):
            finalNode = currNode
            break


        
        #change cost
        #currNode.cost=currNode.cost+currNode.hCol()

        # apply operator
        applyOperator(currNode, notExpanded, nAquariums)

        # selects next node to process
        if notExpanded.isEmpty(): # no more nodes to expand, no solution found
            break
        else:
            currNode = notExpanded.pop()
    
    printAlgorithmResults("A*", start, finalNode)    


    
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

# # ---
# # Blind Algorithms

# bfs(initial_node) # mais ou menos 20s
# dfs(initial_node) # mais ou menos 0.001s
# ucs(initial_node) # mais ou menos 0.002s
# its(initial_node) # mais ou menos 1min

# # ---
# # Heuristic 

def getOption(max):
    option = input("Select an option: ")
    while True:
        try:
            tmp = int(option)
            if (tmp >= 0 and tmp <= max):
                break
            else:
                option = input("Invalid Option! Select an option: ")
        except:
            option = input("Invalid Option! Select an option: ")
        
    return int(option)

def getAquarium(maxAquarium):
    option = input("Select an aquarium(Fill: 1/%d)(Unfill: %d/-1)(Leave Game: 0): " % (maxAquarium, -maxAquarium))
    while True:
        try:
            tmp = int(option)
            if (tmp >= -maxAquarium and tmp <= maxAquarium):
                break
            else:
                option = input("Invalid Option! Select an aquarium(1-%d): " % (maxAquarium))
        except:
            option = input("Invalid Option! Select an aquarium(1-%d): " % (maxAquarium))
        
    return int(option)

def humanMode(initial_node):
    currNode = initial_node
    finalNode = -1

    nAquariums = max([abs(x) for x in set(sum(initial_node.state.aquarium,[]))]) #Number of aquariums

    print("\n&&&&&&&&&&&&&&&&&&&&&")
    print("     LET'S PLAY")
    print("&&&&&&&&&&&&&&&&&&&&&\n")

    while True:
        if isObjective(currNode):
            finalNode = currNode
            break

        printAquarium(currNode)
        aquariumOption = getAquarium(nAquariums)
        if aquariumOption == 0: return
        elif aquariumOption > 0: newAquarium = Fill(currNode, aquariumOption).apply()
        else: newAquarium = Unfill(currNode, aquariumOption).apply()
        while newAquarium == -1:
            if aquariumOption > 0: print("\nIt is not possible to fill that aquarium!", end = "")
            else: print("\nIt is not possible to unfill that aquarium!", end = "")
            aquariumOption = getAquarium(nAquariums)
            if aquariumOption == 0: return
            elif aquariumOption > 0: newAquarium = Fill(currNode, aquariumOption).apply()
            else: newAquarium = Unfill(currNode, aquariumOption).apply()

        currNode = newAquarium
        
    
def pcMode():
    while True:
        print("\n#########################")
        print("     ALGORITHM MENU      ")
        print("#########################")
        
        print("\n1) Breadth First Search")
        print("2) Depth First Search")
        print("3) Uniform Cost Search")
        print("4) Iterative Deepening Search")
        print("5) Greedy Search")
        print("6) A Star")
        print("7) Return")
        print("0) Exit")
        
        option = getOption(7)
        if option == 1: bfs(initial_node)
        elif option == 2: dfs(initial_node)
        elif option == 3: ucs(initial_node)
        elif option == 4: its(initial_node)
        elif option == 5: greedy(initial_node)
        elif option == 6: aStar(initial_node)
        elif option == 7: return 0
        else: return -1

def mainMenu():
    while True:
        print("#########################")
        print("        MAIN MENU        ")
        print("#########################")
        
        print("\n1) Human Mode")
        print("2) PC Mode")
        print("0) Exit")
        
        option = getOption(2)
        if option == 1: humanMode(initial_node)
        elif option == 2:
            if pcMode() == -1:
                return;
        else:
            return;

def game():
    mainMenu()
    
game()
        





