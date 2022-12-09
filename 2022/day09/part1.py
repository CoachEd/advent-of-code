import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')
 
# SOLUTION
# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

def countArr(a):
  count = 0
  for r in a:
    for c in r:
      if c != ' ':
        count += 1
  return count

def printArr(a):
  s = ''
  for r in a:
    for c in r:
      s += c
    s += '\n'
  print(s)

def adj(arr):
  global hy
  global hx
  global ty
  global tx
  for y in range(hy-1,hy+2):
    for x in range(hx-1,hx+2):
      if ty == y and tx == x:
        return True
  return False

def up(arr):
  global hy
  global hx
  global ty
  global tx
  hy -= 1 # move head up
  if not adj(arr):
    # move tail
    ty -= 1
    tx = hx
    
def down(arr):
  global hy
  global hx
  global ty
  global tx
  hy += 1 # move head down
  if not adj(arr):
    # move tail
    ty += 1
    tx = hx
    
def left(arr):
  global hy
  global hx
  global ty
  global tx
  hx -= 1 # move head left
  if not adj(arr):
    # move tail
    tx -= 1
    ty = hy
    
def right(arr):
  global hy
  global hx
  global ty
  global tx
  hx += 1 # move head right
  if not adj(arr):
    # move tail
    tx += 1
    ty = hy


def move(d,n):
  global arr
  for i in range(n):
    if d == 'U':
      up(arr)
    elif d == 'D':
      down(arr)
    elif d == 'L':
      left(arr)
    elif d == 'R':
      right(arr)
    arr[ty][tx] ="#"

rows = 500
cols = 500
(sy,sx) = (int(rows/2), int(cols/2))
arr = [ [' ' for x in range(cols)] for y in range(rows)]

arr[sy][sx] = 's'  # s ior # means visited

(hy,hx) = (sy,sx)
(ty,tx) = (sy,sx)
for s in l:
  a = s.split()
  direction = a[0]
  distance = int(a[1])
  move(direction, distance)

arr[sy][sx] = 's'
#printArr(arr)
print(countArr(arr))

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')