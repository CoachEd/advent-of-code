"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

def print_ocean(arr):
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
arr = [ [ c for c in s ] for s in l ]
print_ocean(arr)

# move east herd
for y in range(rows):
  for x in range(cols):
    c = arr[y][x]
    if not c == '>':
      continue
    newx = x+1
    if newx >= cols:
      newx = 0
    if arr[y][newx] == '.':
      arr[y][x] = '.'
      arr[y][newx] = '>'
      
# move south herd
for y in range(rows):
  for x in range(cols):
    c = arr[y][x]
    if not c == 'v':
      continue
    newy = y+1
    if newy >= rows:
      newy = 0
    if arr[newy][x] == '.':
      arr[y][x] = '.'
      arr[newy][x] = 'v'
print()
print_ocean(arr)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
