# day 11 pt 2
import time
import sys
from copy import copy, deepcopy

# read in input file
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
l=[None for i in range(len(lines))]
for i in range(len(lines)):
  l[i] = lines[i].strip()

def printmap(m):
  s = ''
  for y in range(len(m)):
    for x in range(len(m[y])):
      s += m[y][x]
    s += '\n'
  print(s)

def dist(p1,p2):
  (y0,x0) = p1
  (y1,x1) = p2
  return abs(y0 - y1) + abs(x0 - x1)

def calc():
  global galaxies,distances
  tot = 0
  g = galaxies
  for i in range(len(g)-1):
    for j in range(i+1, len(g)):
      d = dist(g[i],g[j])
      distances.append(d)
      tot += d
  return tot

def getGalaxies(m):
  gnum = 1
  galaxies = []
  for y in range(len(m)):
    for x in range(len(m[y])):
      if m[y][x] == '#':
        galaxies.append((y,x))
        m[y][x] = str(gnum)
        gnum += 1
  return galaxies
  
def expand(N):
  global orig_rows,empty_rows,empty_cols,m
  
  # insert rows N x as large
  m2 = []
  for y in range(orig_rows):
    m2.append(m[y])
    if y in empty_rows:
      for i in range(1,N):
        m2.append(m[y].copy())
  m = m2
 
  # insert cols
  for x in empty_cols:
    for r in m:
      for i in range(1,N):
        r.insert(x,'.')
  return m
  
# SOLUTION START - start timing
start_secs = time.time()

N = 100 # part 1
orig_rows = len(l)
orig_cols = len(l[0])

m0 = [ ['.' for x in range(orig_cols) ] for y in range(orig_rows) ]

# populate
for y in range(orig_rows):
  for x in range(orig_cols):
    m0[y][x] = l[y][x]

empty_rows = []
for y in range(1,orig_rows-1):
  if not '#' in m0[y]:
    empty_rows.append(y) 

empty_cols = []
for x in range(1,orig_cols-1):
  is_empty = True
  for y in range(orig_rows):
    if m0[y][x] == '#':
      is_empty = False
      break
  if is_empty:
    empty_cols.append(x)
empty_cols.sort(reverse=True)

distances = None
d3 = {}
for N in [10,100]:
  distances = []
  m = deepcopy(m0)
  expand(N)
  galaxies = getGalaxies(m)
  d0 = calc()
  print(d0)
  print( (N,distances[0]) )
  d3[N] = distances.copy()

#print(d3) 
d10 = d3[10]
d100 = d3[100]
steps = []
for i in range(len(d10)):
  d1 = d100[i]
  d0 = d10[i]
  steps.append((d1 - d0))

#print(steps)
print('here...')

gtot = 0
N = 100000
for j in range(len(steps)):
  step = steps[j]
  #tot = d10[j]
  #print(d10[j])
  n = 10
  tot = d10[j]
  while n <= N:
    tot += step * n / 10
    n *= 10
  gtot += tot
print(int(gtot))

"""
  #print((d10[j],step,N))
  #z = d100[j] + step * N / 100
  z = d10[j]
  #print(z)
  tot += z
  #for i in range(10,N):
  #  tot += step
print(int(tot))
"""


end_secs = time.time()

print('--- ' + str(end_secs-start_secs) + ' secs ---')

# SOLUTION END - stop timing

# too low 711255130936
