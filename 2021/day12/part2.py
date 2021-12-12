# Part 2

"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

d = {}
ends = ['start','end']
for s in l:
  arr = s.split('-')
  fr = arr[0]
  to = arr[1]
  if fr == 'start':
    if not fr in d.keys():
      d[fr] = []
    d[fr].append(to)
  elif to == 'start':
    if not to in d.keys():
      d[to] = []
    d[to].append(fr)
  elif fr == 'end':
    if not to in d.keys():
      d[to] = []
    d[to].append(fr)
  elif to == 'end':
    if not fr in d.keys():
      d[fr] = []
    d[fr].append(to)
  else:
    if not fr in d.keys():
      d[fr] = []
    if not to in d.keys():
      d[to] = []
    d[fr].append(to)
    d[to].append(fr)

#print(d)

allpaths = []

def smalldups(a):
  counts = {}
  for e in a:
    if not e.islower():
      continue
    if not e in counts.keys():
      counts[e] = 0
    counts[e] += 1
  if len(counts) == 0:
    return False
  for key, value in counts.items():
    if value > 1:
      return True
  return False
  


def paths(s, visited, d):
  if s.islower() and s in visited and smalldups(visited):
    allpaths.append(visited.copy())
    return
  if s == 'end':
    visited1 = visited.copy()
    visited1.append(s)
    allpaths.append(visited1)
    return
  if not s in d:
    allpaths.append(visited.copy())
    return
    
  exits = d[s]
  visited1 = visited.copy()
  visited1.append(s)
  for e in exits:
    paths(e, visited1, d)
  
  
paths('start',[],d)

good = []
for p in allpaths:
  if p[-1] == 'end':
    good.append(','.join(p))
    
print(len(good))



print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')