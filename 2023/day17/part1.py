import time
import sys
import math
from copy import copy, deepcopy

def goodp(y,x,m):
  return y >= 0 and x >= 0 and y < len(m) and x < len(m[0])

def print_map(m):
  s = ''
  for y in range(len(m)):
    for x in range(len(m[y])):
      s += str(m[y][x])
    s += '\n'
  print(s)

def find_paths(starty, startx, endy, endx, m, visited_nodes, directions):
  paths = set()
  if starty == endy and startx == endx:
    print(''.join(directions))
    return

  (ny,nx) = (starty-1,startx)
  (sy,sx) = (starty+1,startx)
  (ey,ex) = (starty,startx+1)
  (wy,wx) = (starty,startx-1)

  


# read in input file
fname = 'inp2.txt'
with open(fname, 'r') as file:
  data = file.read()
lines = data.split('\n')
l=[None for i in range(len(lines))]
for i in range(len(lines)):
  l[i] = lines[i].strip()
#print(l)

# SOLUTION START - start timing
start_secs = time.time()

rows = len(l)
cols = len(l[0])
m = [ [ int(c) for c in row ] for row in l ]
(sx,sy) = (0,0)
(ex,ey) = (rows-1,cols-1)

print_map(m)

find_paths(sy, sx, ey, ex, m, [], [])










end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
# SOLUTION END - stop timing