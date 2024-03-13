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
  
  ds = ['N','S','E','W']
  ps = [(ny,nx),(sy,sx),(ey,ex),(wy,wx)]
  
  for i in range(len(ds)):
    d1 = ds[i]
    (y0,x0) = ps[i]

    if goodp(y0,x0,m) and not (y0,x0) in visited_nodes and directions[-2:].count(d1) != 2:
      d2 = directions.copy()
      v2 = visited_nodes.copy()
      d2.append(d1)
      v2.append((starty,startx))
      find_paths(y0,x0,endy,endx,m,v2,d2)
  
  path1 = ''.join(directions)
  if not path1 in paths and starty == endy and startx == endx:
    paths.add(path1)
    print(path1)

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