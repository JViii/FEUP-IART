from random import randrange
from data_structures.node import Node
from state.state import State
from utils.utils import *


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#       AQUARIUM EXAMPLES
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def getStartingNode():
    r=randrange(4)
    switcher ={
    0:Node(State(copy_list(initialAquarium1), rowCap1, colCap1)),
    1:Node(State(copy_list(initialAquarium2), rowCap2, colCap2)),
    2:Node(State(copy_list(initialAquarium3), rowCap3, colCap3)),
    3:Node(State(copy_list(initialAquarium4), rowCap4, colCap4)),
    }
    return switcher.get(r)


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

# ---
# Ex3
initialAquarium3 = [[-1,-4,-4,-6,-5,-5],
                    [-1,-4,-6,-6,-6,-5],
                    [-1,-4,-4,-4,-5,-5],
                    [-1,-4,-4,-4,-3,-2],
                    [-1,-1,-1,-1,-3,-2],
                    [-1,-2,-2,-2,-2,-2]]

rowCap3 = [3,4,2,3,5,1]
colCap3 = [2,2,3,4,4,3]

# ---
# Ex4
initialAquarium4 = [[-1,-6,-6,-6,-6,-4],
                    [-1,-6,-6,-4,-6,-4],
                    [-1,-1,-1,-4,-6,-4],
                    [-1,-3,-4,-4,-6,-4],
                    [-1,-3,-3,-4,-4,-4],
                    [-2,-2,-2,-4,-5,-5]]

rowCap4 = [4,3,4,3,3,3]
colCap4 = [3,5,4,2,5,1]