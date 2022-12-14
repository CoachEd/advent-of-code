import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

def printCave(a):
  global min_x, min_y, max_x, max_y
  s = ''
  start_y = min_y - 3
  end_y = max_y + 3
  start_x = min_x - 3
  end_x = max_x + 3

  for y in range(start_y, end_y):
    for x in range(start_x, end_x):
      s += a[y][x]
    s += '\n'
  print(s)

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

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

cols = max_x + 5
rows = max_y + 5
cave = [ ['.' for x in range(cols)] for y in range(rows) ]

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


printCave(cave)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')