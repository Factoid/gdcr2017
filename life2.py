import unittest

class Grid:
  def __init__(self):
    self.cells = {}

  def set(self, x,y):
    self.cells[(x,y)] = True

  def get(self, x, y):
    return (x,y) in self.cells

  def clear(self, x, y):
    self.cells.pop( (x,y), None )

  def neighbours(self, x, y):
    count = 0
    for dx in range(-1,2):
      for dy in range(-1,2):
        if dx == 0 and dy==0 :
          continue
        if self.get(x+dx,y+dy) == True:
          count+= 1
    return count

  def getDead(self):
    nGrid = Grid()
    for pos in self.cells.keys():
      for dx in range(-1,2):
        for dy in range(-1,2):
          if dx == 0 and dy == 0: continue
          if self.get( pos[0] + dx, pos[1] + dy ) == False: nGrid.set( pos[0] + dx, pos[1] + dy )
    return nGrid.cells.keys()

  def next(self):
    nGrid = Grid()
    for x,y in self.cells.keys():
      n=self.neighbours(x,y)
      if n ==2 or n == 3: 

class LifeTests(unittest.TestCase):
  def test_cellGetSet(self):
    grid = Grid()
    grid.set(5,5)
    self.assertEqual(grid.get(5,5), True)
    self.assertEqual(grid.get(3,4), False)
    
  def test_cellClear(self):
    grid = Grid()
    grid.set(4,4)
    grid.clear(4,4)
    self.assertEqual(grid.get(4,4), False)

  def test_neghbours(self):
    grid = Grid()
    grid.set(4,4)
    grid.set(4,5)
    grid.set(5,4)
    self.assertEqual(grid.neighbours(4,4), 2)
    self.assertEqual(grid.neighbours(5,4), 2)
    self.assertEqual(grid.neighbours(4,5), 2)
    self.assertEqual(grid.neighbours(5,5), 3)
    self.assertEqual(grid.neighbours(3,3), 1)
    self.assertEqual(grid.neighbours(3,4), 2)
    self.assertEqual(grid.neighbours(2,4), 0)
  
  def test_findDead(self):
    grid = Grid()
    grid.set(4,4)
    grid.set(4,5)
    grid.set(5,4)
    arr = grid.getDead()
    test_arr = [(3,3),(4,3),(5,3),(6,3),(3,4),(6,4),(3,5),(5,5),(6,5),(3,6),(4,6),(5,6)]
    self.assertEqual(len(arr),len(test_arr))
    for v in arr:
      self.assertEqual( v in test_arr, True )

  def test_newBord(self):
    grid = Grid()
    grid.set(4,4)
    grid.set(4,5)
    grid.set(5,4)
    grid.set(5,5)
    
    nGrid = grid.next()
    self.assertEqual(len(nGrid.cells),len(grid.cells))
    for v in nGrid.cells:
      self.assertEqual( v in grid.cells, True )

unittest.main()    
