# day 10 part 1
import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')
 
# SOLUTION

def printMap(a):
  s = ''
  for y in range(rows):
    for x in range(cols):
      s += m[y][x]
    s += '\n'
  print(s)

def goodp(y,x):
  global rows,cols
  if x >= 0 and y >= 0 and x < cols and y < rows:
    return True
  return False

def getPaths(y,x):
  global m,sc
  (n0,n1,s0,s1,e0,e1,w0,w1) = (y-1,x,y+1,x,y,x+1,y,x-1)

  a = []
  
  c = m[y][x]
  if c == 'S':
    c = sc

  if goodp(n0,n1) and m[n0][n1] in 'S|7F' and c in '|LJ':
    a.append((n0,n1))

  if goodp(s0,s1) and m[s0][s1] in 'S|LJ'  and c in '|7F':
    #print(('here','S',s0,s1,m[s0][s1]))
    a.append((s0,s1))
  if len(a) == 2:
    return a
  
  if goodp(e0,e1) and m[e0][e1] in 'S-J7' and c in '-LF':
    a.append((e0,e1))
  if len(a) == 2:
    return a 

  if goodp(w0,w1) and m[w0][w1] in 'S-LF' and c in '-7J':
    a.append((w0,w1))
    return a
  
  
  # should not reach here
  return [(-9,-9),(-9,-9)]

def countPath(y,x):
  global m
  d = {}
  steps = 1
  while True:
    #print((y,x))
    a = getPaths(y,x)
    d[(y,x)] = None
    (y0,x0)= (a[0])
    (y1,x1) = (a[1])
    if (y0,x0) not in d:
      (y,x) = (y0,x0)
      d[(y,x)] = None
      steps += 1
    elif (y1,x1) not in d:
      (y,x) = (y1,x1)
      d[(y,x)] = None
      steps += 1
    else:
      break
  return steps

# read in input file
l=[]

sc = 'F' # test data
fname = 'inp3.txt'
sc = 'L' # real data
fname = 'inp.txt'

my_file = open(fname, "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

rows = len(l)
cols = len(l[0])
(sy,sx) = (-1,-1)
m = [['.' for x in range(cols)] for y in range(rows)]

for y in range(rows):
  for x in range(cols):
    m[y][x] = l[y][x]
    if m[y][x] == 'S':
      (sy,sx) = (y,x)

print(int(countPath(sy,sx) / 2))
 
 
print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')