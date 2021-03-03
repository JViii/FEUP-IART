class Cell:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.full = 0

  def __eq__(self,other):
    return self.x == other.x and self.y == other.y