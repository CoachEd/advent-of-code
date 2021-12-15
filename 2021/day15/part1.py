"""
AoC
"""
import time

# validate coord
def vc(y,x,a):
  if y < 0 or y >= len(a) or x < 0 or x >= len(a[0]):
    return False
  return True

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

rows = len(l)
cols = len(l[0])
nodes = () # tuple
distances = {}

for y in range(rows):
  for x in range(cols):
    nodes = nodes + ( str(y) + ',' + str(x), ) # add tuple to tuple

add_edges(distances,arr)



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
