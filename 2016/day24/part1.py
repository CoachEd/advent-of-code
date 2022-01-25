"""
AoC
"""
import time
import sys
import copy

def valid(y,x,arr):
  if y < 0 or x < 0 or y >= len(arr) or x >= len(arr[0]):
    return False
  if arr[y][x] == '#':
    return False
  return True

def find_target(n,y,x,steps,arr,seen):
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

  for move in moves:
    (y1,x1) = (move[0],move[1])
    if (y1,x1) in seen:
      continue
    if arr[y1][x1] == n:
      steps += 1
      print(steps)
      return
    else:
      arr1 = copy.deepcopy(arr)
      my_char = arr1[y][x]
      arr1[y][x] = '.'
      arr1[y1][x1] = my_char
      seen1 = seen.copy()
      seen1.add( (y1,x1) )
      steps += 1
      find_target(n,y1,x1,steps,arr1,seen1)

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
my_file = open("inp_small.txt", "r", encoding='utf-8')
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


(y,x) = (targets[0][0],targets[0][1])
find_target(4,y,x,0,arr,set())


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
