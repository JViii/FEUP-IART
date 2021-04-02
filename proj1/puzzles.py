from random import randrange
from data_structures.node import Node
from state.state import State
from utils.utils import *


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#       AQUARIUM EXAMPLES
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def getStartingNode():
    r=randrange(6)
    #print("Aq: %d " % (r))
    # r = 6 # 4, 7
    switcher ={
    0:Node(State(copy_list(initialAquarium1), rowCap1, colCap1)),
    1:Node(State(copy_list(initialAquarium2), rowCap2, colCap2)),
    2:Node(State(copy_list(initialAquarium3), rowCap3, colCap3)),
    3:Node(State(copy_list(initialAquarium4), rowCap4, colCap4)),
    4:Node(State(copy_list(initialAquarium5), rowCap5, colCap5)),
    #5:Node(State(copy_list(initialAquarium6), rowCap6, colCap6)),
    6:Node(State(copy_list(initialAquarium7), rowCap7, colCap7)),
    #7:Node(State(copy_list(initialAquarium8), rowCap8, colCap8)),
    #8:Node(State(copy_list(initialAquarium9), rowCap9, colCap9)),
    9:Node(State(copy_list(initialAquarium10), rowCap10, colCap10)),
    }
    return switcher.get(6)

#6x6
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
# Ex4 - Easy
initialAquarium4 = [[-1,-6,-6,-6,-6,-4],
                    [-1,-6,-6,-4,-6,-4],
                    [-1,-1,-1,-4,-6,-4],
                    [-1,-3,-4,-4,-6,-4],
                    [-1,-3,-3,-4,-4,-4],
                    [-2,-2,-2,-4,-5,-5]]

rowCap4 = [4,3,4,3,3,3]
colCap4 = [3,5,4,2,5,1]

#Ex5- Normal 
initialAquarium5 = [[-1, -1, -2, -2, -3, -3],
                    [-2, -2, -2, -3, -3, -3],
                    [-4, -5, -5, -3, -8, -3],
                    [-4, -4, -5, -8, -8, -3],
                    [-6, -4, -5, -7, -9, -3],
                    [-6, -5, -5, -7, -9, -3]]

rowCap5 = [4,3,1,3,4,4]
colCap5 = [4,3,2,4,3,3]

# ---
# Ex6- Hard
initialAquarium6 = [[-1,-1,-1,-1,-2,-2],
                    [-3,-4,-4,-5,-5,-6],
                    [-3,-7,-8,-9,-9,-6],
                    [-7,-7,-8,-10,-11,-11],
                    [-12,-13,-13,-10,-14,-15],
                    [-16,-17,-18,-18,-14,-15]]

rowCap6 = [4,4,4,4,2,3]
colCap6 = [5,3,4,5,3,1]

#10x10
# ---
# Ex7- Easy
initialAquarium7 = [[-1, -2, -3, -4, -4, -4, -4, -4, -4, -7],
                    [-1, -2, -3, -4, -4, -4, -7, -7, -7, -7],
                    [-2, -2, -3, -5, -6, -4, -7, -7, -7, -7],
                    [-8, -8, -8, -5, -6, -6, -6, -7, -9, -7],
                    [-6, -6, -6, -6, -6, -7, -7, -7, -9, -9],
                    [-10,-10,-10,-6, -11,-7, -7, -7, -7, -9],
                    [-10,-12,-10,-11,-11,-11,-11,-7, -7, -7],
                    [-10,-12,-11,-11,-7, -7, -7, -7, -13,-13],
                    [-12,-12,-11,-11,-11,-11,-14,-7, -13,-13],
                    [-12,-12,-12,-12,-12,-11,-14,-13,-13,-13]]

rowCap7 = [9,6,6,8,7,2,5,9,9,9]
colCap7 = [9,7,9,9,8,7,3,5,7,6]


# ---
# Ex8: Hard
initialAquarium8 = [[ -1,  -2,  -2,  -3,  -4,  -5,  -5,  -5,  -5,  -6], #6
                    [ -1,  -1,  -1,  -3,  -4,  -7,  -7,  -8,  -6,  -6], #3
                    [ -9,  -9,  -1,  -1, -10,  -7, -11,  -8, -12, -13], #6
                    [ -9,  -9, -14, -14, -14, -15, -15, -16, -12, -13], #3
                    [-16, -16, -17, -14, -14, -18, -18, -18, -19, -19], #8
                    [-16, -16, -17, -17, -20, -18, -21, -21, -22, -19], #4
                    [-16, -23, -24, -17, -20, -20, -24, -24, -22, -25], #4
                    [-26, -23, -24, -27, -27, -28, -28, -28, -22, -25], #7
                    [-26, -26, -26, -29, -29, -28, -28, -25, -22, -25], #2
                    [-26, -26, -31, -31, -29, -30, -30, -25, -25, -25]] #9
                    #  4    6    6    6    4    7    6    7    3    3

rowCap8 = [6, 3, 6, 3, 8, 4, 4, 7, 2, 9]
colCap8 = [4, 6, 6, 6, 4, 7, 6, 7, 3, 3]

# Ex9 - Hard
initialAquarium9 = [[-1,-2,-3,-3,-3,-3,-3,-4,-4,-4],
                    [-1,-2,-2,-5,-3,-3,-3,-6,-7,-4],
                    [-5,-5,-5,-5,-5,-3,-6,-6,-7,-4],
                    [-8,-8,-5,-9,-10,-10,-11,-11,-12,-13],
                    [-14,-14,-15,-9,-10,-10,-10,-16,-12,-13],
                    [-17,-18,-15,-9,-19,-19,-19,-16,-20,-13],
                    [-21,-18,-22,-23,-23,-23,-24,-20,-20,-20],
                    [-21,-25,-25,-26,-26,-26,-24,-27,-27,-27],
                    [-28,-29,-29,-30,-26,-26,-31,-27,-27,-31],
                    [-28,-32,-32,-30,-33,-33,-31,-31,-31,-31]]

rowCap9 = [2,3,2,6,5,3,6,2,5,9]
colCap9 = [7,7,7,5,2,2,4,2,4,3]

#15x15 
#Ex10 - Easy
initialAquarium10=[ [ -1, -2, -3, -3, -3, -3, -4, -4, -4, -4, -4, -4, -6, -7, -7],
                    [ -1, -2, -3, -3, -2, -2, -4, -4, -5, -4, -4, -4, -6, -7, -7],
                    [ -1, -2, -2, -2, -2, -2, -4, -5, -5, -4, -6, -6, -6, -6, -7],
                    [ -1, -1, -2,-22, -2,-21, -4, -4, -5, -5, -6, -7, -7, -6, -7],
                    [-18, -1, -2,-22,-22,-21, -6, -6, -6, -5, -6, -7, -7, -7, -7],
                    [-18, -1, -2,-22,-22,-21,-20, -6, -6, -6, -6, -6, -8, -7, -7],
                    [-18,-19,-19,-19,-22,-19,-20, -6, -6, -8, -8, -8, -8, -8, -7],
                    [-18,-19,-18,-19,-19,-19,-20,-20,-20, -8, -7, -7, -7, -7, -7],
                    [-18,-18,-18,-17,-19,-19,-17,-17,-17, -8, -9, -9, -9, -9, -7],
                    [-18,-18,-17,-17,-17,-17,-17,-17,-17, -8, -8, -9, -9, -9, -7],
                    [-16,-16,-16,-16,-17,-12,-12,-12,-12,-10,-10, -9, -7, -7, -7],
                    [-16,-15,-15,-16,-13,-11,-11,-10,-10,-10,-10, -9, -9, -7, -7],
                    [-14,-15,-15,-13,-13,-13,-11,-10,-10,-10,-10,-10, -9, -9, -9],
                    [-14,-15,-13,-13,-11,-11,-11,-11,-11,-11,-10,-10,-10,-10, -9],
                    [-14,-14,-13,-13,-13,-13,-13,-10,-10,-10,-10, -9, -9, -9, -9]]

rowCap10 = [7, 9, 5, 6, 2, 8, 3, 4, 4, 11, 5, 6, 1, 11, 11]
colCap10 = [9, 7, 6, 5, 5, 6, 11, 10, 10, 10, 4, 4, 1, 2, 3]



