import time
import sys
import math
from copy import copy, deepcopy

# BEGIN CLASS - ORIGINAL CODE
# keyworkds: Dijkstra, graph, GRAPH, vertice, node, shortest, shortest path
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

def goodp(y,x,m):
  return y >= 0 and x >= 0 and y < len(m) and x < len(m[0])

def print_map(m):
  s = ''
  for y in range(len(m)):
    for x in range(len(m[y])):
      s += str(m[y][x])
    s += '\n'
  print(s)

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
nodes = {}
for y in range(rows):
  for x in range(cols):
    node_name = str(y) + ',' + str(x)
    nodes[node_name] = m[y][x]

input_vertices = ()  # tuple of all unique node names
input_graph = {}  # dictionary of edges
for node_name,v in nodes.items():
  fr = node_name
  if not fr in input_vertices:
    input_vertices = input_vertices + (fr,)
  if not node_name in input_graph:
    input_graph[node_name] = {}

# add edges and weights
for y in range(rows):
  for x in range(cols):
    node_name = str(y) + ',' + str(x)
    (uy,ux) = (y-1,x)
    (dy,dx) = (y+1,x)
    (ry,rx) = (y,x+1)
    (ly,lx) = (y,x-1)

    (y0,x0) = (uy,ux)
    if goodp(y0,x0,m):
      to_node_name = str(y0) + ',' + str(x0)
      input_graph[node_name][to_node_name] = m[y0][x0]  # add edge with weight
    
    (y0,x0) = (dy,dx)
    if goodp(y0,x0,m):
      to_node_name = str(y0) + ',' + str(x0)
      input_graph[node_name][to_node_name] = m[y0][x0]  # add edge with weight

    (y0,x0) = (ry,rx)
    if goodp(y0,x0,m):
      to_node_name = str(y0) + ',' + str(x0)
      input_graph[node_name][to_node_name] = m[y0][x0]  # add edge with weight

    (y0,x0) = (ly,lx)
    if goodp(y0,x0,m):
      to_node_name = str(y0) + ',' + str(x0)
      input_graph[node_name][to_node_name] = m[y0][x0]  # add edge with weight                

def find_all_paths(graph, start, end, path=[]):
  path = path + [start]
  if start == end:
    return [path]
  if start not in graph:
    return []
  paths = []
  for node in graph[start]:
    if node not in path:
      newpaths = find_all_paths(graph, node, end, path)
      for newpath in newpaths:
        paths.append(newpath)
  return paths    


# MAIN
start_vertex = '0,0'
end_vertex = '12,12'

paths = find_all_paths(input_graph,start_vertex,end_vertex)
print(len(paths))












end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
# SOLUTION END - stop timing