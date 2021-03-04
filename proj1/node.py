class Node:
    def __init__(self, state, parent = -1, depth = 0, cost = 0):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.cost = cost