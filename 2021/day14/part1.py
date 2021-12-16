# part 1


"""
AoC
"""
import time
import sys
from copy import copy, deepcopy
d = {}
counts = {}

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

s = l[0]
for i in range(2,len(l)):
  a = l[i].split(' -> ')
  d[ a[0] ] = a[1]

# get initial counts
for c in s:
  if not c in counts:
    counts[c] = 0
  counts[c] += 1

# add initial edges
edges = {}
for i in range(0,len(s)-1):
  edge = s[i] + s[i+1]
  if not edge in edges:
    edges[edge] = 0
  edges[edge] += 1

# steps - apply each rule to all edges
steps = 10
for step in range(  steps ):
  edges2 = {}
  for e in edges:
    if e in d:
      # inserts
      c0 = e[0]
      c1 = e[1]
      insrt = d[e]
      num = edges[e]
      e0 = c0 + insrt
      e1 = insrt + c1    
      if not e0 in edges2:
        edges2[e0] = 0
      if not e1 in edges2:
        edges2[e1] = 0
      edges2[e0] += num
      edges2[e1] += num
      if not insrt in counts:
        counts[insrt] = 0
      counts[insrt] = counts[insrt] + num
    else:
      # carry over
      if not e in edges2:
        edges2[e] = 0
      edges2[e] += edges[e]
  edges = edges2.copy()

# get answer
mx = 0
mn = sys.maxsize
for key in counts:
  if counts[key] > mx:
    mx = counts[key]
  if counts[key] < mn:
    mn = counts[key]

print(str(mx-mn))

end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
