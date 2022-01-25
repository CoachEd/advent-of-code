"""
AoC
"""
import time
import sys
import copy

found = False
def valid(y,x,arr):
  if y < 0 or x < 0 or y >= len(arr) or x >= len(arr[0]):
    return False
  if arr[y][x] == '#':
    return False
  return True

def find_target(n,y,x,steps,arr,seen):
  global found
  if found:
    return
  (ty,tx,by,bx,ry,rx,ly,lx) = (y-1,x,y+1,x,y,x+1,y,x-1)
  seen.add((y,x))
  moves = []
  if valid(ty,tx,arr):
    moves.append([ty,tx])
  if valid(by,bx,arr):
    moves.append([by,bx])
  if valid(ry,rx,arr):
    moves.append([ry,rx])
  if valid(ly,lx,arr):
    moves.append([ly,lx])

  new_steps = steps
  for move in moves:
    (y1,x1) = (move[0],move[1])
    if (y1,x1) in seen:
      continue
    new_steps = steps + 1
    if arr[y1][x1] == n:
      found = True
      print('steps: ' + str(new_steps) +   '   0 y,x: ' + str((y1,x1)))
      return
    else:
      arr1 = copy.deepcopy(arr)
      my_char = arr1[y][x]
      arr1[y][x] = '.'
      arr1[y1][x1] = my_char
      seen1 = seen.copy()
      seen1.add( (y1,x1) )
      find_target(n,y1,x1,new_steps,arr1,seen1)

def print_map(arr):
  s = ''
  for row in arr:
    for c in row:
      s += c
    s += '\n'
  print(s)

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

rows = len(l)
cols = len(l[0])
arr = [[' ' for x in range(cols)] for y in range(rows)]

targets = {}  # dictionary target 0-7 (int), [y,x] int,int

for y in range(rows):
  for x in range(cols):
    c = l[y][x]
    if c.isnumeric():
      c = int(c)
      targets[c] = [y,x]
    arr[y][x] = c


# 0 to 4
(y,x) = (targets[0][0],targets[0][1])
find_target(4,y,x,0,arr,set())
# OUTPUT: steps: 90   0 y,x: (17, 165)

# 0 to 5
"""
arr[y][x] = '.'
targets[0][0] = 17
targets[0][1] = 165
(y,x) = (targets[0][0],targets[0][1])
arr[y][x] = 0
find_target(5,y,x,0,arr,set())
# OUTPUT: ?
"""


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
