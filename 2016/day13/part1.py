"""
AoC
"""
import time
import sys
import math
from copy import copy, deepcopy

start_secs = time.time()
print('')

inp = 1364
rows = 100
cols = 100

# test data
#inp = 10
#rows = 7
#cols = 10


# validate coord
def vc(y,x,a):
  if y < 0 or y >= len(a) or x < 0 or x >= len(a[0]):
    return False
  return True

# add edge
def add_edge(y1,x1,y2,x2,a,d):
  if not vc(y1,x1,a) or not vc(y2,x2,a) or a[y2][x2] == 1 or a[y1][x1] == 1 or (y1 == y2 and x1 == x2):
    return
  n1 = str(y1)+','+str(x1)
  n2 = str(y2)+','+str(x2)
  if not n1 in d:
    d[n1] = {}
  if not n2 in d:
    d[n2] = {}
  
  if not n2 in d[n1]:
    # add it
    d[n1][n2] = 1

  if not n1 in d[n2]:
    # add it
    d[n2][n1] = 1

# add edges, distance,array
def add_edges(d,a):
  for y in range(len(a)):
    for x in range(len(a[y])):

      if a[y][x] == 1:
        # wall
        continue

      ty = y-0
      tx = x
      by = y+1
      bx = x
      ry = y
      rx = x+1
      ly = y
      lx = x-1
      
      add_edge(y,x,ty,tx,a,d)
      add_edge(y,x,by,bx,a,d)
      add_edge(y,x,ry,rx,a,d)
      add_edge(y,x,ly,lx,a,d)

def get_cell(y,x):
  global inp
  n = x*x + 3*x + 2*x*y + y + y*y
  n += inp
  s = "{0:b}".format(n)
  cnt = s.count('1')
  return (cnt % 2)  # 0 means space, 1 means wall

def print_board(arr):
  s = ''
  for row in arr:
    for n in row:
      if n == 1:
        s += '#'
      else:
        s += '.'
    s += '\n'
  print(s)

a = [ [0 for x in range(cols)] for y in range(rows) ]
for y in range(rows):
  for x in range(cols):
    a[y][x] = get_cell(y,x)

nodes = () # tuple
distances = {}

for y in range(rows):
  for x in range(cols):
    if a[y][x] == 0:
      nodes = nodes + ( str(y) + ',' + str(x), ) # add tuple to tuple

add_edges(distances,a)
print_board(a)
for key, value in distances.items():
    print(str(key) + ': ' + str(value))
print()

# try
unvisited = {node: None for node in nodes} #using None as +inf
visited = {}
current = '1,1'
currentDistance = 0
unvisited[current] = currentDistance

while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited: continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited: break
    candidates = [node for node in unvisited.items() if node[1]]
    if len(candidates) == 0:
      break
    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

dest = '39,31'
print(visited[dest])




print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
