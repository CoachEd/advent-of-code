"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

# validate coord
def vc(y,x,a):
  if y < 0 or y >= len(a) or x < 0 or x >= len(a[0]):
    return False
  return True

def print_map(arr):
  s = ''
  for r in arr:
    for e in r:
      s += str(e)
    s += '\n'
  print(s)

# add panel
def add_panel(arr,oarr,y1,x1,n):
  arr2 = bump_up_array(oarr,n)

  for y in range(0,len(arr2)):
    for x in range(0,len(arr2[0])):
      dy = y+y1
      dx = x+x1
      arr[dy][dx] = arr2[y][x]

# add edge
def add_edge(y1,x1,y2,x2,a,d):
  if not vc(y1,x1,a) or not vc(y2,x2,a):
    return
  n1 = str(y1)+','+str(x1)
  n2 = str(y2)+','+str(x2)
  if not n1 in d:
    d[n1] = {}
  if not n2 in d:
    d[n2] = {}
  
  if not n2 in d[n1]:
    # add it
    d[n1][n2] = a[y2][x2]

  if not n1 in d[n2]:
    # add it
    d[n2][n1] = a[y1][x1]

# add edges, distance,array
def add_edges(d,a):
  for y in range(len(a)):
    for x in range(len(a[y])):
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

def bump_up_array(a,n):
  a2 = deepcopy(a)
  for y in range(len(a)):
    for x in range(len(a[y])):
      r = a[y][x]
      for i in range(n):
        r = r + 1
        if r == 10:
          r = 1
      a2[y][x] = r
  return a2

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

arr = []
for y in range(len(l)):
  arrtemp =[]
  for x in range(len(l[y])):
    arrtemp.append(int(l[y][x]))
  arr.append(arrtemp)

orows = len(l)
ocols = len(l[0])

# expand array
rows = orows * 5
cols = ocols * 5
arrbig = [ [0 for x in range(cols)] for y in range(rows) ]
for y in range(len(arr)):
  for x in range(len(arr[y])):
    arrbig[y][x] = arr[y][x]

# add 1 to the right
#add_panel(arrbig,arr,0,0+len(arr[0]),1)

bumpval = [
[0,1,2,3,4],
[1,2,3,4,5],
[2,3,4,5,6],
[3,4,5,6,7],
[4,5,6,7,8]
]

n = 0
by = 0
bx = 1
for y in range(0,len(arrbig),len(arr)):
  for x in range(0,len(arrbig[y]),len(arr[0])):
    if y == 0 and x == 0:
      continue
    add_panel(arrbig,arr,y,x,bumpval[by][bx])
    bx += 1
  by += 1
  bx = 0

nodes = () # tuple
distances = {}

for y in range(rows):
  for x in range(cols):
    nodes = nodes + ( str(y) + ',' + str(x), ) # add tuple to tuple

add_edges(distances,arrbig)



# try
unvisited = {node: None for node in nodes} #using None as +inf
visited = {}
current = '0,0'
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
    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

dest = str(cols-1)+','+str(rows-1)
print(visited[dest])

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')

""" 30.55 mins
$ python part2.py

3045

--- 1833.0013060569763 secs ---
$
"""