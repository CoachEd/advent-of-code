import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

def next_pos_t(y,x,ns,ew,a):
  if len(ns) > 0:
    # can only go either e or w
    (ry, rx) = (y, x+1)
    (ly, lx) = (y, x-1)
    if valid(ry, rx, a) and a[ry][rx] != ' ':
      return ( (ry, rx, '', 'e') )
    if valid(ly, lx, a) and a[ly][lx] != ' ':
      return ( (ly, lx, '', 'w') )
  elif len(ew) > 0:
    # can only go n or s
    (ty, tx) = (y-1, x)
    (by, bx) = (y+1, x)
    if valid(ty,tx,a) and a[ty][tx] != ' ':
      return( (ty, tx, 'n', '') )
    if valid(by, bx, a) and a[by][bx] != ' ':
      return ( (by, bx, 's', '') )

def next_pos(y,x,ns,ew):
  if len(ns) > 0:
    if ns == 'n':
      return (y-1, x)
    elif ns == 's':
      return (y+1, x)
  elif len(ew) > 0:
    if ew == 'e':
      return (y, x+1)
    elif ew == 'w':
      return (y, x-1)

def valid(y,x,a):
  if x < 0 or y < 0 or x >= len(a[0]) or y >= len(a):
    return False
  return True

def done(y,x,seen,a):
  (y0, x0) = (y, x+1)
  (y1, x1) = (y, x-1)
  (y2, x2) = (y+1, x)
  (y3, x3) = (y-1, x)
  a = [ (y0, x0), (y1, x1), (y2, x2), (y3, x3)]
  for (ytemp, xtemp) in a:
    if (ytemp, xtemp) in seen:
      continue
    if valid(ytemp, xtemp, a):
      if arr[ytemp][xtemp] != ' ':
        return True
  return False


# SOLUTION
# read in input file
max_cols = 0
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  if len(line) > max_cols:
    max_cols = len(line)
  l.append(line.rstrip())

arr = [ [ ' ' for x in range(max_cols) ] for y in range(len(l)) ]
for y in range(len(l)):
  for x in range(len(l[y])):
    arr[y][x] = l[y][x]

# print - testing
"""
s = ''
for y in range(len(arr)):
  for x in range(len(arr[y])):
    s += arr[y][x]
  s += '\n'
print(s)
"""

# get starting point
y = 0
x = 0
for i in range(len(l[0])):
  if arr[y][i] == '|':
    x = i
    break

seen = set()
letters = ''
x1 = 0
y1 = 0
(prev_y, prev_x) = (0, 0)
ns = 's'
ew = ''
while True:
  c = arr[y][x]
  if c.isalpha():
    letters += c
    (y1, x1) = next_pos(y,x,ns,ew)
  elif c == '|':
    (y1, x1) = next_pos(y,x,ns,ew)
  elif c == '-':
    (y1, x1) = next_pos(y,x,ns,ew)
  elif c == '+':
   (y1, x1, ns, ew) = next_pos_t(y,x,ns,ew,arr)

  (prev_y, prev_x) = (y, x)
  x = x1
  y = y1

  if arr[y][x] == ' ':
    break

print(letters)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')