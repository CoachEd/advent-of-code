import time
import sys
import math
from copy import copy, deepcopy
import heapq
start_secs = time.time()
print('')

# keyworkds: Dijkstra, graph, GRAPH, vertice, node, shortest, shortest path

# BEGIN CLASS - ORIGINAL CODE
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

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

input_vertices = ()
input_graph = {} 
for s in l:
  arr1 = s.split(' <-> ')
  fr = arr1[0].strip()
  if not fr in input_vertices:
    input_vertices = input_vertices + (fr,)
  tos = arr1[1].split(', ')
  for t in tos:
    if not t in input_vertices:
      input_vertices = input_vertices + (t,)

for nodename in input_vertices:
  if not nodename in input_graph:
    input_graph[nodename] = {}



for s in l:
  arr1 = s.split(' <-> ')
  fr = arr1[0].strip()
  tos = arr1[1].split(', ')
  for t in tos:
    nodeList1 = input_graph[fr]
    nodeList2 = input_graph[t]
    nodeList1[t] = 1
    nodeList2[fr] = 1


# MAIN
start_vertex = '0'
total = 0
for end_vertex in input_vertices:
  dijkstra = Dijkstra(input_vertices, input_graph)

  p, v = dijkstra.find_route(start_vertex, end_vertex)

  # check if NO path
  dist = v[end_vertex]
  if (math.isinf(dist)):
    # this path is an infinite cycle
    #print('error - no path from %s to %s' % (start_vertex, end_vertex) )
    continue

  total += 1
  print(start_vertex + ' -> ' + end_vertex)
  """
  print()
  se = dijkstra.generate_path(p, start_vertex, end_vertex)
  print("Path from %s to %s is:\n%s" % (start_vertex, end_vertex, " -> ".join(se)))
  print('distance: %.2f' % (dist))
  print('steps: %s' % str(len(se)-1))
  """

print()
print(total)


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')