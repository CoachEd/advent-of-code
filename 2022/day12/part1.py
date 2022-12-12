import time
import sys
from copy import copy, deepcopy
import heapq
start_secs = time.time()
print('')

# BEGIN CLASS
class Dijkstra:
  def __init__(self, vertices, graph):
    self.vertices = vertices  # ("A", "B", "C" ...)
    self.graph = graph  # {"A": {"B": 1}, "B": {"A": 3, "C": 5} ...}

  def find_route(self, start, end):
    unvisited = {n: float("inf") for n in self.vertices}
    unvisited[start] = 0  # set start vertex to 0
    visited = {}  # list of all visited nodes
    parents = {}  # predecessors
    while unvisited:
      min_vertex = min(unvisited, key=unvisited.get)  # get smallest distance
      for neighbour, _ in self.graph.get(min_vertex, {}).items():
        if neighbour in visited:
          continue
        new_distance = unvisited[min_vertex] + self.graph[min_vertex].get(neighbour, float("inf"))
        if new_distance < unvisited[neighbour]:
          unvisited[neighbour] = new_distance
          parents[neighbour] = min_vertex
      visited[min_vertex] = unvisited[min_vertex]
      unvisited.pop(min_vertex)
      if min_vertex == end:
        break
    return parents, visited

  @staticmethod
  def generate_path(parents, start, end):
    path = [end]
    while True:
      key = parents[path[0]]
      path.insert(0, key)
      if key == start:
        break
    return path
# END CLASS

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

# create names for all vertices, e.g. row,col '0,1'
input_vertices = ()
for y in range(rows):
  for x in range(cols):
    nodeName = str(y) + ',' + str(x)
    input_vertices = input_vertices + (nodeName,)
# create graph, e.g.
"""
input_graph = {
  "A": {"B": 5, "D": 3, "E": 12, "F": 5},
  "B": {"A": 5, "D": 1, "G": 2},
  "C": {"E": 1, "F": 16, "G": 2},
  "D": {"A": 3, "B": 1, "E": 1, "G": 1},
  "E": {"A": 12, "C": 1, "D": 1, "F": 2},
  "F": {"A": 5, "C": 16, "E": 2},
  "G": {"B": 2, "C": 2, "D": 1}
}
"""

input_graph = {} # dictionary of dictionaries
weights = {}
for c in 'abcdefghijklmnopqrstuvwxyz':
  weights[c] = ord(c)
weights['S'] = ord('a')
weights['E'] = ord('z')

for y in range(rows):
  for x in range(cols):
    nodename = str(y) + ',' + str(x)
    if not nodename in input_graph:
      input_graph[nodename] = {}
    
    nodeList = input_graph[nodename]  # this nodes list of neighbors
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

start_vertex = str(sy) + ',' + str(sx)
end_vertex= str(ey) + ',' + str(ex)

dijkstra = Dijkstra(input_vertices, input_graph)

p, v = dijkstra.find_route(start_vertex, end_vertex)
print("Distance from %s to %s is: %.2f" % (start_vertex, end_vertex, v[end_vertex]))

se = dijkstra.generate_path(p, start_vertex, end_vertex)
print("Path from %s to %s is: %s" % (start_vertex, end_vertex, " -> ".join(se)))
print()
print('steps %s' % str(len(se)-1))

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')