import sys
import time
import os

WIDTH = 10
HEIGHT = 10
state = [False] * WIDTH * HEIGHT

def getCell( x, y, stateArray ):
  return stateArray[y*WIDTH+x]

def setCell( x, y, value, stateArray ):
  stateArray[y*WIDTH+x] = value

def liveNeighbours( x, y, stateArray ):
  totalLive = 0
  for dx in range(-1,2):
    for dy in range(-1,2):
      if( dx == 0 and dy == 0 ): continue
      if( x + dx < 0 or x + dx >= WIDTH ): continue
      if( y + dy < 0 or y + dy >= HEIGHT ): continue
      #print( "Checking cell", x + dx, y + dy )
      if( getCell( x + dx, y + dy, stateArray ) == True ): totalLive += 1
  return totalLive

def nextGeneration( stateArray ):
  nextStateArray = [False] * len(stateArray)
  for x in range(WIDTH):
    for y in range(HEIGHT):
      n = liveNeighbours(x,y,stateArray)
      if( getCell( x, y, stateArray ) == True ):
        setCell( x, y, ( n == 2 or n == 3 ), nextStateArray )
      else:
        setCell( x, y, ( n == 3 ), nextStateArray )
  return nextStateArray

def showCells( stateArray ):
  for y in range(HEIGHT):
    for x in range(WIDTH):
      if( getCell(x,y,stateArray) == False ):
        sys.stdout.write("  ")
      else:
        sys.stdout.write("😄 ")
    sys.stdout.write("\n")

def writeGlider( x,y, stateArray ):
  setCell(x+2,y,True,stateArray)
  setCell(x,y+1,True,stateArray)
  setCell(x+1,y+1,True,stateArray)
  setCell(x+1,y+2,True,stateArray)
  setCell(x+2,y+2,True,stateArray)

writeGlider(2,2,state)
for i in range(8):
  os.system('clear')
  showCells( state )
  state = nextGeneration(state)
  time.sleep(0.5)
