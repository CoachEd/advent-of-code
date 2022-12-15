import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

def countSand(a):
  global min_x, min_y, max_x, max_y
  count = 0
  start_y = 0
  end_y = max_y + 3
  start_x = min_x - 3
  end_x = max_x + 3

  for y in range(start_y, end_y):
    for x in range(start_x, end_x):
      if a[y][x] == 'O':
        count += 1
  return count

def printCave(a):
  global min_x, min_y, max_x, max_y, found_void
  s = ''
  start_y = min_y - 4
  end_y = max_y + 3
  start_x = min_x - 3
  end_x = max_x + 3
  for y in range(start_y, end_y):
    for x in range(start_x, end_x):
      s += a[y][x]
    s += '\n'
  print(s)

def dropSand(a):
  global sand_x, sand_y, min_x, min_y, max_x, max_y, found_void
  x = sand_x
  y = sand_y
  while True:

    if y == 0 and x == 500 and a[y+1][x-1] == 'O' and a[y+1][x] == 'O' and  a[y+1][x+1] == 'O':
      a[y][x] = 'O'
      found_void = True
      return

    if a[y][x] == 'O':
      if y > max_y or x < min_x or x > max_x:
        # endless void
        a[y][x] = '.'
        found_void = True
        return

    if a[y+1][x] != '.' and a[y+1][x-1] != '.' and a[y+1][x+1] != '.':
      return
    
    if a[y+1][x] != '.' and a[y+1][x-1] == '.':
      # move diagonally down left
      a[y][x] = '.'
      a[y+1][x-1] = 'O'
      y = y+1
      x = x-1
    elif a[y+1][x] != '.' and a[y+1][x+1] == '.':
      # move diagonally down right
      a[y][x] = '.'
      a[y+1][x+1] = 'O'
      y = y+1
      x = x+1     
    elif a[y+1][x] == '.':
      # move down
      a[y][x] = '.'
      a[y+1][x] = 'O'
      y = y+1

    printCave(a)



# MAIN

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

found_void = False
sand_x = 500
sand_y = 0
max_x = -1
max_y = -1
min_x = sys.maxsize
min_y = sys.maxsize
for s in l:
  arr = s.split(' -> ')
  for p in arr:
    arr2 = p.split(',')
    x = int(arr2[0])
    y = int(arr2[1])
    if x < min_x:
      min_x = x
    if y < min_y:
      min_y = y
    if x > max_x:
      max_x = x
    if y > max_y:
      max_y = y

cols = max_x + 20
rows = max_y + 20
cave = [ ['.' for x in range(cols)] for y in range(rows) ]
cave[sand_y][sand_x] = '+'

floor_y = max_y + 2
floor_x0 = min_x - 10
floor_x1 = max_x + 13
min_x = floor_x0
max_x = floor_x1
max_y = floor_y
for i in range(floor_x0,floor_x1):
  cave[floor_y][i] = '#'

for s in l:
  arr = s.split(' -> ')
  for i in range(len(arr)-1):
    arr0 = arr[i].split(',')
    x0 = int(arr0[0])
    y0 = int(arr0[1])
    arr0 = arr[i+1].split(',')
    x1 = int(arr0[0])
    y1 = int(arr0[1])

    if (y0 == y1):
      # across
      start = x1
      end = x0
      if x0 < x1:
        start = x0
        end = x1
      for x in range(start, end+1):
        cave[y0][x] = '#'

    if (x0 == x1):
      # down
      start = y1
      end = y0
      if y0 < y1:
        start = y0
        end = y1
      for y in range(start, end+1):
        cave[y][x0] = '#'

while not found_void:
  dropSand(cave)

printCave(cave)

print( countSand(cave) )
# 699 WRONG TOO LOW

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')