"""
AoC
"""
import time
import sys
import copy


# validate coord
def vc(y,x,a):
  if y < 0 or y >= len(a) or x < 0 or x >= len(a[0]):
    return False
  return True

# add edge
def add_edge(y1,x1,y2,x2,a,d):
  if not vc(y1,x1,a) or not vc(y2,x2,a) or (y1 == y2 and x1 == x2):
    return
  if a[y1][x1] == '#' or a[y2][x2] == '#':
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

      if a[y][x] == '#':
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


def print_map(arr):
  s = ''
  for row in arr:
    for c in row:
      s += c
    s += '\n'
  print(s)

def path(y0,x0,y1,x1):
  unvisited = {node: None for node in nodes} #using None as +inf
  visited = {}
  current = str(y0) + ',' + str(x0)
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

  dest = str(y1) + ',' + str(x1)
  return visited[dest]

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

rows = len(l)
cols = len(l[0])
arr = [[' ' for x in range(cols)] for y in range(rows)]

targets = {}  # dictionary target 0-7 (int), [y,x] int,int

for y in range(rows):
  for x in range(cols):
    c = l[y][x]
    if c.isnumeric():
      c = int(c)
      targets[c] = [y,x]
    arr[y][x] = c
# targets:
# {0: [1, 175], 2: [3, 49], 1: [7, 7], 4: [17, 165], 3: [19, 1], 7: [31, 11], 5: [31, 177], 6: [33, 43]}
print(targets)

nodes = () # tuple
for y in range(rows):
  for x in range(cols):
    if arr[y][x] != '#':
      nodes = nodes + ( str(y) + ',' + str(x), ) # add tuple to tuple

distances = {}
add_edges(distances,arr)
"""
for key, value in distances.items():
  print(str(key) + ': ' + str(value))
print()
"""

# try
steps = 0
A=0
(y0,x0) = (targets[A][0],targets[A][1])
for B in range(8):
  if B != 4:
    continue
  (y1,x1) = (targets[B][0],targets[B][1])
  steps1 = path(y0,x0,y1,x1)
  steps += steps1
  print(str(A) + ' -> ' + str(B) + ':  ' + str(steps1) )

A=4
(y0,x0) = (targets[A][0],targets[A][1])
for B in range(8):
  if B != 5:
    continue
  (y1,x1) = (targets[B][0],targets[B][1])
  steps1 = path(y0,x0,y1,x1)
  steps += steps1
  print(str(A) + ' -> ' + str(B) + ':  ' + str(steps1) )

A=5
(y0,x0) = (targets[A][0],targets[A][1])
for B in range(8):
  if B != 6:
    continue
  (y1,x1) = (targets[B][0],targets[B][1])
  steps1 = path(y0,x0,y1,x1)
  steps += steps1
  print(str(A) + ' -> ' + str(B) + ':  ' + str(steps1) )

A=6
(y0,x0) = (targets[A][0],targets[A][1])
for B in range(8):
  if B != 2:
    continue
  (y1,x1) = (targets[B][0],targets[B][1])
  steps1 = path(y0,x0,y1,x1)
  steps += steps1
  print(str(A) + ' -> ' + str(B) + ':  ' + str(steps1) )

A=2
(y0,x0) = (targets[A][0],targets[A][1])
for B in range(8):
  if B != 3:
    continue
  (y1,x1) = (targets[B][0],targets[B][1])
  steps1 = path(y0,x0,y1,x1)
  steps += steps1
  print(str(A) + ' -> ' + str(B) + ':  ' + str(steps1) )

A=3
(y0,x0) = (targets[A][0],targets[A][1])
for B in range(8):
  if B != 1:
    continue
  (y1,x1) = (targets[B][0],targets[B][1])
  steps1 = path(y0,x0,y1,x1)
  steps += steps1
  print(str(A) + ' -> ' + str(B) + ':  ' + str(steps1) )

A=1
(y0,x0) = (targets[A][0],targets[A][1])
for B in range(8):
  if B != 7:
    continue
  (y1,x1) = (targets[B][0],targets[B][1])
  steps1 = path(y0,x0,y1,x1)
  steps += steps1
  print(str(A) + ' -> ' + str(B) + ':  ' + str(steps1) )

print(steps)
# 454 too high

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
