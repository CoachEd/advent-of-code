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
groups = 0

while True:
  if len(input_vertices) == 0:
    break
  start_vertex = input_vertices[0]
  total = 0
  input_vertices2 = ()
  for end_vertex in input_vertices:
    dijkstra = Dijkstra(input_vertices, input_graph)

    p, v = dijkstra.find_route(start_vertex, end_vertex)

    # check if NO path
    dist = v[end_vertex]
    if (math.isinf(dist)):
      # this path is an infinite cycle
      #print('error - no path from %s to %s' % (start_vertex, end_vertex) )
      input_vertices2 = input_vertices2 + (end_vertex,)
      continue

    total += 1
    """
    print()
    se = dijkstra.generate_path(p, start_vertex, end_vertex)
    print("Path from %s to %s is:\n%s" % (start_vertex, end_vertex, " -> ".join(se)))
    print('distance: %.2f' % (dist))
    print('steps: %s' % str(len(se)-1))
    """

  groups += 1
  print('progs: ' + str(total))
  input_vertices = input_vertices2

print(groups)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')