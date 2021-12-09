# Part 1
"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

def v(a,y,x):
  if y >= 0 and y < len(a) and x >= 0 and x < len(a[0]):
    return True
  return False

def lowpoint(a,y,x):
  n = a[y][x]
  yt = y-1
  xt = x
  yb = y+1
  xb = x
  yr = y
  xr = x+1
  yl = y
  xl = x-1
  
  y1 = yt
  x1 = xt
  if v(a,y1,x1) and a[y1][x1] <= n:
    return False
  
  y1 = yb
  x1 = xb
  if v(a,y1,x1) and a[y1][x1] <= n:
    return False
    
  y1 = yr
  x1 = xr
  if v(a,y1,x1) and a[y1][x1] <= n:
    return False
    
  y1 = yl
  x1 = xl
  if v(a,y1,x1) and a[y1][x1] <= n:
    return False
    
  return True
    

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

a = []
for r in l:
  a1 = []
  for e in r:
    a1.append(int(e))
  a.append(a1)

risk = 0
for y in range(len(a)):
  for x in range(len(a[y])):
    if lowpoint(a,y,x):
      risk += (a[y][x] + 1)
      
print(risk)
      
# 1737

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')