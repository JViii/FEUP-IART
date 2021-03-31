from state.state import State
from data_structures.node import Node
from operators.fill import Fill
from operators.unfillhuman import UnfillHuman
from operators.fillhuman import FillHuman
from utils.utils import *
from data_structures.priority_queue import PriorityQueue
from data_structures.myqueue import Queue
from data_structures.stack import Stack
from puzzles import *

from time import *

import numbers

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

MAX_REPEATED = 5000
repeated_nodes = []

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#       PRINT FUNCTIONS
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# ---
# Prints the Aquarium
def printAquarium(node):
    aquarium = node.state.aquarium
    rowCap = node.state.rowCap
    colCap = node.state.colCap

    print("\n-----------------")
    for i in range(len(aquarium)):
        for j in range(len(aquarium)):
            print("%3d" % (aquarium[i][j]), end = " ")
        print("| %d" % (rowCap[i]))
    
    print("-----------------")
    for i in range(len(aquarium)):
         print("%3d" % (colCap[i]), end = " ")

    print("\n $$$ Moves: %d" % (node.exp))


    print("\n")

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
      
def getOldestRepeated():
    ret = -1
    old = -1
    for i in range(len(repeated_nodes)):
        if old < repeated_nodes[i][1]:
            old = repeated_nodes[i][1]
            ret = i
    return ret


def incRepeatedNodes():
    for i in range(len(repeated_nodes)):
        repeated_nodes[i][1] += 1

# ---
# Verifies if a state is repeated
# A state can is repeated when:
#   we have already fill a cell belonging to the same aquarium in the same iteration(verification done in applyOperator)
#   we have cousins exatly with same aquarium cells filled
def isRepeated(node):
    for i in range(len(repeated_nodes)):
        if compare_lists(repeated_nodes[i][0].state.aquarium, node.state.aquarium):
            repeated_nodes[i][1] = 0
            return True

    if len(repeated_nodes) == MAX_REPEATED:
        ind = getOldestRepeated()
        repeated_nodes[ind] = [node, 0]
    else:
        repeated_nodes.append([node, 0])

    return False

# -----------

# ---
# Applies all the possible operators to the corresponding state
def applyOperator(node, notExpanded, nAquariums, allowedDepth = -1, alg = "blind"):
    aquarium = node.state.aquarium
    childrenNumber = 0
    
    # Verifies if we reach the max depth
    # Only used for iterative deepening search
    if node.depth == allowedDepth:
        return; 

    incRepeatedNodes()

    for i in range(1,nAquariums+1):
      newNode = Fill(node, i).apply()
      if newNode != -1 and not isRepeated(newNode):
        # newNode.setChildrenNumber(childrenNumber) # necessary to test if it's repeated
        # if not isRepeated(newNode):
            # printAquarium(newNode)
            # node.addChildren(newNode)
            if alg == "blind" or (alg != "blind" and newNode.heuristic < 1000):
                notExpanded.push(newNode)
            # childrenNumber += 1

# -----------

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

    repeated_nodes = []

    start = time()
    
    print("\nSolving using BFS...")

    while True:
        if isObjective(currNode):
            finalNode = currNode
            break
        print("&&&&&&&&&&&&&")
        printAquarium(currNode)

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

    repeated_nodes = []

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

    notExpanded = PriorityQueue()

    repeated_nodes = []

    start = time()
    
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
    notExpanded = Stack()
    depth = 0

    start = time()
    
    print("\nSolving using ITS...")

    repeated_nodes = []

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

    repeated_nodes = []

    start = time()
    print("\nSolving using Greedy Search...")

    while True:
        if isObjective(currNode):
            finalNode = currNode
            break

        # print("&&&&&&&&&&&&&")
        #printAquarium(currNode)

        # apply operator
        applyOperator(currNode, notExpanded,nAquariums, "heuristic")

        # selects next node to process
        if notExpanded.isEmpty(): # no more nodes to expand, no solution found
            break
        else:
            currNode = notExpanded.pop()
    
    printAlgorithmResults("Greedy", start, finalNode)    

# ---
# A* 
def aStar(initial_node, human_mode = False):
    currNode = initial_node
    finalNode = -1

    nAquariums = max([abs(x) for x in set(sum(initial_node.state.aquarium,[]))]) #Number of aquariums

    notExpanded = PriorityQueue("aStar")

    repeated_nodes = []

    start = time()
    if not human_mode: print("\nSolving using A*...")
    # num = 0
    while True:
        # # print("Num: %d" % (num))
        # num += 1
        if isObjective(currNode):
            finalNode = currNode
            break
        # sleep(1)
        # print("&&&&&&&&&&&&&")
        printAquarium(currNode)
        # apply operator
        applyOperator(currNode, notExpanded, nAquariums, "heuristic")

        # selects next node to process
        if notExpanded.isEmpty(): # no more nodes to expand, no solution found
            break
        else:
            currNode = notExpanded.pop()
    
    if not human_mode: printAlgorithmResults("A*", start, finalNode)   
    else: return finalNode
    
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#          ALGORITHMS
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def getOption(max):
    option = input("\nSelect an option: ")
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
    option = input("Select an aquarium(Fill: 1/%d)(Unfill: %d/-1)(Leave Game: 0)(?: Hint): " % (maxAquarium, -maxAquarium))
    while True:
        if option == "?": return "?"
        try:
            tmp = int(option)
            if (tmp >= -maxAquarium and tmp <= maxAquarium):
                break
            else:
                option = input("Invalid aquarium! Select an aquarium(1-%d): " % (maxAquarium))
        except:
            option = input("Invalid aquarium! Select an aquarium(1-%d): " % (maxAquarium))
        
    return int(option)

def numAquariumsFilled(result):
    aquarium = result.state.aquarium
    ret = [0] * len(aquarium)
    
    for i in range(len(aquarium)):
        aq = []
        for j in range(len(aquarium)):
            if not (abs(aquarium[i][j]) in aq) and (aquarium[i][j] > 0):
                aq.append(abs(aquarium[i][j]))
                ret[abs(aquarium[i][j]) - 1] += 1
        aq = []
                
    return ret

def getHint(aquariumsFilled, node):
    currAquariumsFilled = numAquariumsFilled(node)
    
    # Verifie aquariums to unfill
    for i in range(len(currAquariumsFilled)):
        if currAquariumsFilled[i] > aquariumsFilled[i]:
            return str(-(i+1))
        
    # Verifie aquariums to fill
    for i in range(len(currAquariumsFilled)):
        if currAquariumsFilled[i] < aquariumsFilled[i]:
            return str(i+1)
        
def move(currNode, nAquariums, aquariumsFilled):
    printAquarium(currNode)
    aquariumOption = getAquarium(nAquariums)
    
    newAquarium = -1
    
    if aquariumOption == "?": 
        print("Hint: %s" % (getHint(aquariumsFilled, currNode)))
    elif aquariumOption == 0: 
        return 0
    elif aquariumOption > 0: 
        newAquarium = FillHuman(currNode, aquariumOption).apply()
    else: 
        newAquarium = UnfillHuman(currNode, aquariumOption).apply()
    
    while newAquarium == -1:
        if aquariumOption != "?":
            if aquariumOption > 0: 
                print("Aquarium: %d is already completely filled!\n" % (aquariumOption), end = "")
            else: 
                print("Aquarium: %d is already completely unfilled!\n" % (aquariumOption), end = "")
        
        aquariumOption = getAquarium(nAquariums)
        
        if aquariumOption == "?": 
            print("Hint: %s" % (getHint(aquariumsFilled, currNode)))
        elif aquariumOption == 0: 
            return 0
        elif aquariumOption > 0: 
            newAquarium = FillHuman(currNode, aquariumOption).apply()
        else: 
            newAquarium = UnfillHuman(currNode, aquariumOption).apply()
        
    return newAquarium

def humanMode(initial_node):
    currNode = initial_node
    finalNode = -1
    
    result = aStar(initial_node, True)
    aquariumsFilled = numAquariumsFilled(result)
    # print(aquariumsFilled)

    nAquariums = max([abs(x) for x in set(sum(initial_node.state.aquarium,[]))]) #Number of aquariums

    print("\n&&&&&&&&&&&&&&&&&&&&&")
    print("     LET'S PLAY")
    print("&&&&&&&&&&&&&&&&&&&&&\n")

    while True:
        if isObjective(currNode):
            finalNode = currNode
            break
        
        currNode = move(currNode, nAquariums, aquariumsFilled)
        if currNode == 0: return
        
    print("\n\nCONGRATULATIONS!!! YOU HAVE SOLVED THE PUZZLE!!!\n\n")
          
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
    
# Starting Node
initial_node = getStartingNode()
game()
# print(a.get([[1, 2]]))
# a = [1]
# a.insert(0, 2)
# print(a)        





