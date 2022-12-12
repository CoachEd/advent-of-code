import time
import sys
from copy import copy, deepcopy
import heapq
start_secs = time.time()
print('')

# Dijkstra’s algorithm example
def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

def printMap(a):
  s = ''
  for y in range(len(a)):
    for x in range(len(a[y])):
      s += a[y][x]
    s += '\n'
  print(s)

def validPoint(y,x,a):
  rows = len(a)
  cols = len(a[0])
  if y < 0 or x < 0 or y >= rows or x >= cols:
    return False
  return True


# SOLUTION
# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

rows = len(l)
cols = len(l[0])

(sy,sx) = (0,0)
(ey,ex) = (0,0)
for y in range(rows):
  for x in range(cols):
    if l[y][x] == 'S':
      (sy,sx) = (y,x)
    elif l[y][x] == 'E':
      (ey,ex) = (y,x)

# CREATE graph (dictionary of dictionaries), for example
"""
example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}
"""
theGraph = {} # dictionary of dictionaries
weights = {}
for c in 'abcdefghijklmnopqrstuvwxyz':
  weights[c] = ord(c)
weights['S'] = ord('a')
weights['E'] = ord('z')

for y in range(rows):
  for x in range(cols):
    nodename = str(y) + ',' + str(x)
    if not nodename in theGraph:
      theGraph[nodename] = {}
    
    nodeList = theGraph[nodename]  # this nodes list of neighbors
    nodeWeight = weights[l[y][x]] # additional restriction is that neighbor must be at most one more than my weight

    # neighbors
    (uy,ux) = (y-1,x)
    (dy,dx) = (y+1,x)
    (ry,rx) = (y,x+1)
    (ly,lx) = (y,x-1)

    # create edge from node to UP neighbor
    (ty,tx) = (uy,ux)
    if validPoint(ty,tx,l):
      weight = weights[l[ty][tx]]
      if (nodeWeight + 1) >= weight:
        neighborName = str(ty) + ',' + str(tx)
        nodeList[neighborName] = weight

    # create edge from node to DOWN neighbor
    (ty,tx) = (dy,dx)
    if validPoint(ty,tx,l):
      weight = weights[l[ty][tx]]
      if (nodeWeight + 1) >= weight:
        neighborName = str(ty) + ',' + str(tx)
        nodeList[neighborName] = weight

    # create edge from node to RIGHT neighbor
    (ty,tx) = (ry,rx)
    if validPoint(ty,tx,l):
      weight = weights[l[ty][tx]]
      if (nodeWeight + 1) >= weight:
        neighborName = str(ty) + ',' + str(tx)
        nodeList[neighborName] = weight

    # create edge from node to LEFT neighbor
    (ty,tx) = (ly,lx)
    if validPoint(ty,tx,l):
      weight = weights[l[ty][tx]]
      if (nodeWeight + 1) >= weight:
        neighborName = str(ty) + ',' + str(tx)
        nodeList[neighborName] = weight

startNode = str(sy) + ',' + str(sx)
danswer = calculate_distances(theGraph, startNode)
print(danswer[str(ey)+','+str(ex)])

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')