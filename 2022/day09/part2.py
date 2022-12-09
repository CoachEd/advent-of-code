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
  # adjusts all knots except for head
  global knots
  i = j - 1
  if not adj(knots[i], knots[j]):
    if d == 'U':
      knots[j][0] -= 1
      knots[j][1] = knots[i][1]
    elif d == 'D':
      knots[j][0] += 1
      knots[j][1] = knots[i][1]
    elif d == 'L':
      knots[j][1] -= 1
      knots[j][0] = knots[i][0]
    elif d == 'R':
      knots[j][1] += 1
      knots[j][0] = knots[i][0]

    if j == len(knots)-1:
      # tail
      arr[knots[j][0]][knots[j][1]] = "#"

def adjust2(arr,j,d):
  global knots
  i = j - 1 # head
  if not adj(knots[i], knots[j]):
    (hy,hx) = (knots[i][0],knots[i][1])
    (ty,tx) = (knots[j][0],knots[j][1])
    if (hy < ty and abs(hy-ty) > 1):
      # move tail up
      knots[j][0] -= 1
      knots[j][1] = knots[i][1]
    elif (hy > ty and abs(hy-ty) > 1):
      # move tail down
      knots[j][0] += 1
      knots[j][1] = knots[i][1]
    elif (hx < tx and abs(hx-tx) > 1):
      # move tail left
      knots[j][1] -= 1
      knots[j][0] = knots[i][0]
    elif (hx > tx and abs(hx-tx) > 1):
      # move tail right
      knots[j][1] += 1
      knots[j][0] = knots[i][0]      

    if j == len(knots)-1:
      # tail
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

def adj(hd, tl):
  for y in range(hd[0]-1,hd[0]+2):
    for x in range(hd[1]-1,hd[1]+2):
      if tl[0] == y and tl[1] == x:
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
      adjust2(arr,i,d)


# MAIN
rows = 500 #500
cols = 500
numKnots = 10
(sy,sx) = (int(rows/2), int(cols/2))
arr = [ ['.' for x in range(cols)] for y in range(rows)]
arr[sy][sx] = 's'  # s ior # means visited
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
# 2382 too high

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')