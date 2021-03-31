from random import randrange
from data_structures.node import Node
from state.state import State
from utils.utils import *


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#       AQUARIUM EXAMPLES
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def getStartingNode():
    # r=randrange(4)
    r = 6
    switcher ={
    0:Node(State(copy_list(initialAquarium1), rowCap1, colCap1)),
    1:Node(State(copy_list(initialAquarium2), rowCap2, colCap2)),
    2:Node(State(copy_list(initialAquarium3), rowCap3, colCap3)),
    3:Node(State(copy_list(initialAquarium4), rowCap4, colCap4)),
    4:Node(State(copy_list(initialAquarium5), rowCap5, colCap5)),
    5:Node(State(copy_list(initialAquarium6), rowCap6, colCap6)),
    6:Node(State(copy_list(initialAquarium7), rowCap7, colCap7)),
    7:Node(State(copy_list(initialAquarium8), rowCap8, colCap8)),
    8:Node(State(copy_list(initialAquarium9), rowCap9, colCap9)),
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

# ---
# Ex5: 10x10 Hard
initialAquarium5 = [[ -1,  -2,  -2,  -3,  -4,  -5,  -5,  -5,  -5,  -6],
                    [ -1,  -1,  -1,  -3,  -4,  -7,  -7,  -8,  -6,  -6],
                    [ -9,  -9,  -1,  -1, -10,  -7, -11,  -8, -12, -13],
                    [ -9,  -9, -14, -14, -14, -15, -15, -16, -12, -13],
                    [-16, -16, -17, -14, -14, -18, -18, -18, -19, -19],
                    [-16, -16, -17, -17, -20, -18, -21, -21, -22, -19],
                    [-16, -23, -24, -17, -20, -20, -24, -24, -22, -25],
                    [-26, -23, -24, -27, -27, -28, -28, -28, -22, -25],
                    [-26, -26, -26, -29, -29, -28, -28, -25, -22, -25],
                    [-26, -26, -31, -31, -29, -30, -30, -25, -25, -25]]

rowCap5 = [6, 3, 6, 3, 8, 4, 4, 7, 2, 9]
colCap5 = [4, 6, 6, 6, 4, 7, 6, 7, 3, 3]

# Ex6 - Hard
initialAquarium6 = [[-1,-2,-3,-3,-3,-3,-3,-4,-4,-4],
                    [-1,-2,-2,-5,-3,-3,-3,-6,-7,-4],
                    [-5,-5,-5,-5,-5,-3,-6,-6,-7,-4],
                    [-8,-8,-5,-9,-10,-10,-11,-11,-12,-13],
                    [-14,-14,-15,-9,-10,-10,-10,-16,-12,-13],
                    [-17,-18,-15,-9,-19,-19,-19,-16,-20,-13],
                    [-21,-18,-22,-23,-23,-23,-24,-20,-20,-20],
                    [-21,-25,-25,-26,-26,-26,-24,-27,-27,-27],
                    [-28,-29,-29,-30,-26,-26,-31,-27,-27,-31],
                    [-28,-32,-32,-30,-33,-33,-31,-31,-31,-31]]

rowCap6 = [2,3,2,6,5,3,6,2,5,9]
colCap6 = [7,7,7,5,2,2,4,2,4,3]

# ---
# Ex7- 6x6 hard
initialAquarium7 = [[-1,-1,-1,-1,-2,-2],
                    [-3,-4,-4,-5,-5,-6],
                    [-3,-7,-8,-9,-9,-6],
                    [-7,-7,-8,-10,-11,-11],
                    [-12,-13,-13,-10,-14,-15],
                    [-16,-17,-18,-18,-14,-15]]

rowCap7 = [4,4,4,4,2,3]
colCap7 = [5,3,4,5,3,1]

# ---
# Ex8- 10x10 easy

initialAquarium8 = [[-1, -2, -3, -4, -4, -4, -4, -4, -4, -7],
                    [-1, -2, -3, -4, -4, -4, -7, -7, -7, -7],
                    [-2, -2, -3, -5, -6, -4, -7, -7, -7, -7],
                    [-8, -8, -8, -5, -6, -6, -6, -7, -9, -7],
                    [-6, -6, -6, -6, -6, -7, -7, -7, -9, -9],
                    [-10,-10,-10,-6, -11,-7, -7, -7, -7, -9],
                    [-10,-12,-10,-11,-11,-11,-11,-7, -7, -7],
                    [-10,-12,-11,-11,-7, -7, -7, -7, -13,-13],
                    [-12,-12,-11,-11,-11,-11,-14,-7, -13,-13],
                    [-12,-12,-12,-12,-12,-11,-14,-13,-13,-13]]

rowCap8 = [9,6,6,8,7,2,5,9,9,9]
colCap8 = [9,7,9,9,8,7,3,5,7,6]

# Ex9- 6x6 normal -> demora +/- 38s
initialAquarium9 = [[-1, -1, -2, -2, -3, -3],
                    [-2, -2, -2, -3, -3, -3],
                    [-4, -5, -5, -3, -8, -3],
                    [-4, -4, -5, -8, -8, -3],
                    [-6, -4, -5, -7, -9, -3],
                    [-6, -5, -5, -7, -9, -3]]

rowCap9 = [4,3,1,3,4,4]
colCap9 = [4,3,2,4,3,3]

