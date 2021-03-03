class Aquarium:
    def __init__(self, pos):
        self.pos = pos
    
    def findCell(self, cell):
        for i in range(len(pos)):
            if pos[i] == cell:
                return True
        return False