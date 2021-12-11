

# Part 2
"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

flashes = 0
def vnode(a,y,x):
  if y >= 0 and y < len(a) and x >= 0 and x < len(a[0]):
    return True
  return False

def fnb(a,y,x):
  global flashes
  ytl = y-1
  xtl = x-1
  yt = y-1
  xt = x
  ytr = y-1
  xtr = x+1
  yl = y
  xl = x-1
  yr = y
  xr = x+1
  ybl = y+1
  xbl = x-1
  yb = y+1
  xb = x
  ybr = y+1
  xbr = x+1
  nbrs = [ [ytl,xtl], [yt,xt], [ytr,xtr], [yl,xl], [yr,xr], [ybl,xbl], [yb,xb], [ybr,xbr] ]
  flashed = []
  for coord in nbrs:
    y1 = coord[0]
    x1 = coord[1]
    if not vnode(a,y1,x1):
      continue
    if a[y1][x1] == 0:
      continue
    a[y1][x1] += 1
    if a[y1][x1] > 9:
      flashed.append([y1,x1])
      a[y1][x1] = 0
      flashes += 1
  return flashed

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

a =[]
for r in l:
  row = []
  for c in r:
    row.append(int(c))
  a.append(row)

step = 0
while True:
  a1 = deepcopy(a)
  
  # increase all by 1
  for y in range(len(a1)):
    for x in range(len(a1[y])):
      a1[y][x] += 1
      
  flashed = []
  for y in range(len(a1)):
    for x in range(len(a1[y])):
      if a1[y][x] > 9:
        flashed.append([y,x])
        a1[y][x] = 0
        flashes += 1
        
  while len(flashed) > 0:
    flashed2 =[]
    for coord in flashed:
      flashed2 += fnb(a1,coord[0],coord[1])
    flashed = flashed2.copy()
      
  step += 1
  a = deepcopy(a1)
  tot = 0
  for y in range(len(a)):
    for x in range(len(a[y])):
      tot += a[y][x]
  if tot == 0:
    print(step)
    break

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')