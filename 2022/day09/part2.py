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

def adjust(arr,j,d):
  global knots
  i = j - 1
  (hy,hx) = (knots[i][0],knots[i][1])

  if not adj(arr, knots[i], knots[j]):
    if d == 'U':
      knots[j][0] -= 1
      knots[j][1] = hx
    elif d == 'D':
      knots[j][0] += 1
      knots[j][1] = hx
    elif d == 'L':
      knots[j][1] -= 1
      knots[j][0] = hy
    elif d == 'R':
      knots[j][1] += 1
      knots[j][0] = hy

    if j == len(knots)-1:
      arr[knots[j][0]][knots[j][1]] = "#"

def countArr(a):
  count = 0
  for r in a:
    for c in r:
      if c == 's' or c == '#':
        count += 1
  return count

def printArr(a):
  s = ''
  for r in a:
    for c in r:
      s += c
    s += '\n'
  print(s)

def adj(arr, hd, tl):
  (hy,hx) = (hd[0],hd[1])
  (ty,tx) = (tl[0],tl[1])
  for y in range(hy-1,hy+2):
    for x in range(hx-1,hx+2):
      if ty == y and tx == x:
        return True
  return False

def up(hd):
  hd[0] -= 1 # move head up
    
def down(hd):
  hd[0] += 1 # move head down
    
def left(hd):
  hd[1] -= 1 # move head left
    
def right(hd):
  hd[1] += 1 # move head right

def move(d,n,knots):
  global arr
  hd=knots[0]
  for j in range(n):
    if d == 'U':
      up(hd)
    elif d == 'D':
      down(hd)
    elif d == 'L':
      left(hd)
    elif d == 'R':
      right(hd)
    for i in range(1, len(knots)):
      adjust(arr,i,d)


# MAIN
rows = 8 #500
cols = 12
numKnots = 2
(sy,sx) = (int(rows/2), int(cols/2))
arr = [ ['.' for x in range(cols)] for y in range(rows)]
arr[sy][sx] = 's'  # s ior # means visited
(hy,hx) = (sy,sx)
(ty,tx) = (sy,sx)
knots = [ [sy,sx] for x in range(numKnots) ]
for s in l:
  a = s.split()
  direction = a[0]
  distance = int(a[1])
  move(direction,distance,knots)

arr[sy][sx] = 's'
printArr(arr)
print(countArr(arr))
# 6457 too high

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')