class Coord:
  def __init__(x,y):
    self.x = x
    self.y = y

  def X():
    return self.x

  def Y():
    return self.y

  def __eq__(self,other):
    return self.x == other.x and self.y == other.y

board = [
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]
        ]

maxWaterPerLine = [1,5,2,5,3,1]
maxWaterPerCol = [4,3,3,2,2,3]

aquario1 = [ Coord(0,5), Coord(1,5), Coord(2,5), Coord(3,5), Coord(4,5) ]
aquario2 = [ Coord(5,0), Coord(5,4), Coord(4,4), Coord(3,4), Coord(5,3), Coord(5,2), Coord(4,2) ]

aquarios = [aquario1,aquario2] #...


def canFill(aquario,cell):
  if(board[cell.y,cell.x]==1)
    return false

  line = board[cell.y]
  col = board[cell.x]

  if(line.count(1) < maxWaterPerLine[cell.y] and col.count(1) < maxWaterPerCol[cell.x]):
    return noAirBelow(cell)
  else:
    return false
  
def noAirBelow(aquario,cell):
  for c in aquario:
    if(c.y<cell.y and board[c.y][c.x]==0)
      return false
  
  return true

def airOnSides(aquario,cell):
  lista = [ c for ce in aquario if ce.x=cell.x]
  for c in lista
    
  return lista



def fill(x,y):
  board[x][y]=1


