#day 10 part 2
import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')
 
# SOLUTION

def printMap(a):
  global rows,cols
  s = ''
  for y in range(rows):
    for x in range(cols):
      s += m[y][x]
    s += '\n'
  print(s)

def printMap2(a):
  global rows,cols,pipes
  s = ''
  for y in range(rows):
    for x in range(cols):
      c = m[y][x]
      if not (y,x) in pipes:
        s += '.'
      elif c in '-|':
        s += c
      else:
        #s += c
        s += '+'
        
    s += '\n'
  print(s)

def cleanUp(a):
  global rows,cols,pipes
  for y in range(rows):
    for x in range(cols):
      c = m[y][x]
      if not (y,x) in pipes:
        m[y][x] = '.'
      else:
        m[y][x] = c

def printAround(y,x,a,n):
  global rows,cols
  s = 'around ' + str((y,x)) +'\n'
  for y0 in range(y-n,y+n+1):
    for x0 in range(x-n,x+n+1):
      if goodp(y0,x0):
        s += a[y0][x0]
    if y0 >= 0 and y0 < rows:
      s += '\n'
  print(s)

def fillInside(y,x):
  global m,rows,cols,seen
  m[y][x] = 'I'
  # y,x is arbitrary point inside
  (n0,n1,s0,s1,e0,e1,w0,w1) = (y-1,x,y+1,x,y,x+1,y,x-1)
  
  (y0,x0) = (n0,n1)
  if goodp(y0,x0) and m[y0][x0] == '.' and not (y0,x0) in seen:
    seen[(y0,x0)] = None
    m[y0][x0] = 'I'
    fillInside(y0,x0)
    
  (y0,x0) = (s0,s1)
  if goodp(y0,x0) and m[y0][x0] == '.' and not (y0,x0) in seen:
    seen[(y0,x0)] = None
    m[y0][x0] = 'I'
    fillInside(y0,x0)
    
  (y0,x0) = (e0,e1)
  if goodp(y0,x0) and m[y0][x0] == '.' and not (y0,x0) in seen:
    seen[(y0,x0)] = None
    m[y0][x0] = 'I'
    fillInside(y0,x0)
    
  (y0,x0) = (w0,w1)
  if goodp(y0,x0) and m[y0][x0] == '.' and not (y0,x0) in seen:
    seen[(y0,x0)] = None
    m[y0][x0] = 'I'
    fillInside(y0,x0)

def goodp(y,x):
  global rows,cols
  if x >= 0 and y >= 0 and x < cols and y < rows:
    return True
  return False

def getPaths(y,x):
  global m,sc,found
  (n0,n1,s0,s1,e0,e1,w0,w1) = (y-1,x,y+1,x,y,x+1,y,x-1)

  a = []
  
  c = m[y][x]
  if c == 'S':
    c = sc

  if goodp(n0,n1) and m[n0][n1] in 'S|7F' and c in '|LJ':
    a.append((n0,n1))

  if goodp(s0,s1) and m[s0][s1] in 'S|LJ'  and c in '|7F':
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
  global m,pipes,moves
  d = {}
  steps = 1
  while True:
    #print((y,x))
    pipes[(y,x)] = None
    a = getPaths(y,x)
    d[(y,x)] = None
    (y0,x0)= (a[0])
    (y1,x1) = (a[1])
    if (y0,x0) not in d:
      (y,x) = (y0,x0)
      d[(y,x)] = None
      moves.append((y,x))
      steps += 1
    elif (y1,x1) not in d:
      (y,x) = (y1,x1)
      d[(y,x)] = None
      moves.append((y,x))
      steps += 1
    else:
      break
  return steps

# read in input file
l=[]

sc = 'F' # test data
fname = 'inp3.txt'
sc = 'F' # test data
fname = 'inp2.txt'
sc = 'L' # real data
fname = 'inp.txt'
seen = {}
moves = []

my_file = open(fname, "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

pipes = {}
rows = len(l)
cols = len(l[0])
(sy,sx) = (-1,-1)
m = [['.' for x in range(cols)] for y in range(rows)]

for y in range(rows):
  for x in range(cols):
    m[y][x] = l[y][x]
    if m[y][x] == 'S':
      (sy,sx) = (y,x)


countPath(sy,sx)


# Part 2
found = []
cleanUp(m)

(y0,x0) = (sy,sx)
for (y,x) in moves:
  (n0,n1,s0,s1,e0,e1,w0,w1) = (y-1,x,y+1,x,y,x+1,y,x-1)
  
  """
  # S-E - TEST DATA SCENARIO 
  if y == (y0-1):
    # moved N
    if goodp(w0,w1) and m[w0][w1] == '.':
      m[w0][w1] = 'I'
      found.append((w0,w1))
  elif y == (y0+1):
    # moved S
    if goodp(e0,e1) and m[e0][e1] == '.':
      m[e0][e1] = 'I'
      found.append((e0,e1))
  elif x == (x0+1):
    # moved E
    if goodp(n0,n1) and m[n0][n1] == '.':
      m[n0][n1] = 'I'
      found.append((n0,n1))
  elif x == (x0-1):
    # moved W
    if goodp(s0,s1) and m[s0][s1] == '.':
      m[s0][s1] = 'I'
      found.append((s0,s1))
      
  """

  # s - w real data scenario
  if y == (y0-1):
    # moved N
    if goodp(e0,e1) and m[e0][e1] == '.':
      m[e0][e1] = 'I'
      found.append((e0,e1))
  elif y == (y0+1):
    # moved S
    if goodp(w0,w1) and m[w0][w1] == '.':
      m[w0][w1] = 'I'
      found.append((w0,w1))
  elif x == (x0+1):
    # moved E
    if goodp(s0,s1) and m[s0][s1] == '.':
      m[s0][s1] = 'I'
      found.append((s0,s1))
  elif x == (x0-1):
    # moved W
    if goodp(n0,n1) and m[n0][n1] == '.':
      m[n0][n1] = 'I'
      found.append((n0,n1))
      
      
  (y0,x0) = (y,x)


# for each I
for (y,x) in found:
  seen = {}
  fillInside(y,x)

printMap(m)

count = 0
for y in range(rows):
  for x in range(cols):
    if m[y][x] == 'I':
      count += 1
print(count)

#print()
#printAround(sy,sx,m,4)
#591 too low
print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')