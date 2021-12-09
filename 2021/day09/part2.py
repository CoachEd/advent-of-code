# Part 2
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


def basin(a,y,x,v1):
  
  if not v(a,y,x):
    return 0
  
  n = a[y][x]
  if n == 9 or n <= v1:
    return 0
  
  yt = y-1
  xt = x
  yb = y+1
  xb = x
  yr = y
  xr = x+1
  yl = y
  xl = x-1
  
  a[y][x] = 9 # visited
  
  return 1 + basin(a,yt,xt,n) + basin(a,yb,xb,n) + basin(a,yr,xr,n) + basin(a,yl,xl,n)

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

lowpoints = []
for y in range(len(a)):
  for x in range(len(a[y])):
    if lowpoint(a,y,x):
      lowpoints.append([y,x])

b = []
for lp in lowpoints:
  y = lp[0]
  x = lp[1]
  bsize = basin(a,y,x,-1)
  if bsize > 0:
    b.append(bsize)


b.sort()
x = b[-1]
y = b[-2]
z = b[-3]
print(x*y*z)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')

