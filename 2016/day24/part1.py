"""
AoC
"""
import time
import sys
import copy
from itertools import permutations


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

def get_path(A,B):
  (y0,x0) = (targets[A][0],targets[A][1])
  (y1,x1) = (targets[B][0],targets[B][1])
  return path(y0,x0,y1,x1)

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
#print(targets)

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

# 5 to others
arr = [0,5,4,2,3,1,7,6] # 
A = arr[-1]
for i in range(0,8):
  if i in arr:
    continue
  print(str(A) + ' -> ' + str(i) + '  ' + str(get_path(A,i)) + ' steps.' )
print()
"""
0 -> 1  266 steps.
0 -> 2  208 steps.
0 -> 3  252 steps.
0 -> 4  26 steps. *****
0 -> 5  44 steps. *****
0 -> 6  196 steps.
0 -> 7  246 steps.
"""


# try
steps = 0
orders1 = [''.join(p) for p in permutations('12367')]
orders2 = [ '045'+s for s in orders1 ]
orders3 = [ '054'+s for s in orders1 ]
orders = orders2 + orders3
print('orders: ' + str(len(orders)))
print()

order_num = 1
for order in orders:
  steps = 0
  for i in range(0,len(order)-1):
    A=int(order[i])
    B=int(order[i+1])
    (y0,x0) = (targets[A][0],targets[A][1])
    (y1,x1) = (targets[B][0],targets[B][1])
    steps += path(y0,x0,y1,x1)
  print(str(order_num) + '.  order: ' + order + '    steps = ' + str(steps))
  order_num += 1

# order: 04513627    steps = 550
# order: 04513267    steps = 538
# order: 04531762    steps = 504
# order: 04573126    steps = 492
# 466 too high: 04526317
# 458 too high: 05462317
# 454 too high: 04562317
# 446 too high: 04526731
#   04562137    steps = 442 RIGHT!!!!
#
# 402 too low

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
