import sys
import time
import math
from copy import copy, deepcopy
import cProfile, pstats
from io import StringIO

"""
pr = cProfile.Profile()  # create a profile object
pr.enable()  # start profiling
"""

start_secs = time.time()

s = """.#..#
.#.#.
#..##
.#.##
##..#"""

arr = s.split('\n')
print(arr)

def valid(x,y,arr):
  if x < 0 or y < 0 or x >= len(arr[0]) or y >= len(arr):
    return False
  return True

def getBoard(arr):
  s = '\n'
  for r in arr:
    for c in r:
      s = s + c
    s = s + '\n'
  return s

def getNeighbors(x,y,arr):
  ux=x
  uy=y-1
  rx=x+1
  ry=y
  lx=x-1
  ly=y
  dx=x
  dy=y+1
  neighbors = 0
  if valid(ux,uy,arr) and arr[uy][ux] == '#':
    neighbors = neighbors + 1
  if valid(dx,dy,arr) and arr[dy][dx] == '#':
    neighbors = neighbors + 1
  if valid(rx,ry,arr) and arr[ry][rx] == '#':
    neighbors = neighbors + 1
  if valid(lx,ly,arr) and arr[ly][lx] == '#':
    neighbors = neighbors + 1
  return neighbors


steps = 100
print('t' + str(0) + ': ' + getBoard(arr))

layouts = []
layouts.append(getBoard(arr))
for t in range(1,steps+1):
  next_arr = []
  for y in range(len(arr)):
    temp_arr = []
    for x in range(len(arr[y])):
      #A bug dies (becoming an empty space) unless there is exactly one bug adjacent to it.
      #An empty space becomes infested with a bug if exactly one or two bugs are adjacent to it.
      #Otherwise, a bug or empty space remains the same.
      neighbors = getNeighbors(x,y,arr)
      if arr[y][x] == '#' and neighbors != 1:
        temp_arr.append('.')
      elif arr[y][x] == '.' and (neighbors == 1 or neighbors == 2):
        temp_arr.append('#')
      else:
        temp_arr.append(arr[y][x])
    next_arr.append(temp_arr)
  arr = next_arr
  new_board = getBoard(arr)
  if new_board in layouts:
    print('found: ' + new_board)
    break
  else:
    layouts.append(new_board)
  #print('t' + str(t) + ': ' + getBoard(arr))

# calculate biodiversity rating
"""
Each of these tiles is worth biodiversity points equal to increasing powers of two: 1, 2, 4, 8, 16, 32, and so on. 
Add up the biodiversity points for tiles with bugs; in this example, the 16th tile (32768 points) and 
22nd tile (2097152 points) have bugs, a total biodiversity rating of 2129920.
"""
tile_num = 0
bd_rating = 0
for y in range(len(arr)):
  for x in range(len(arr[y])):
    bdpoints = 2 ** tile_num
    if arr[y][x] == '#':
      bd_rating = bd_rating + bdpoints
    tile_num = tile_num + 1
print(bd_rating)



    

    

"""
pr.disable()  # end profiling

# print out some stats.
s = StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
"""

end_secs = time.time()
print('elapsed time: ' + str(end_secs - start_secs) + ' seconds')
