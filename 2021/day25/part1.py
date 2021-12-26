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

steps = 1000000
for i in range(steps):
  movement = False
  for y in range(rows):
    for x in range(cols):
      c = arr[y][x]
      if c == '>':
        newx = x + 1
        if newx >= cols:
          newx = 0
        if arr[y][newx] == '.':
          arr[y][x] = 'X'
          arr[y][newx] = 'R'
          movement = True
  for y in range(rows):
    for x in range(cols):
      if arr[y][x] == 'R':
        arr[y][x] = '>'
      elif arr[y][x] == 'X':
        arr[y][x] = '.'
  for y in range(rows):
    for x in range(cols):
      c = arr[y][x]
      if c == 'v':
        newy = y + 1
        if newy >= rows:
          newy = 0
        if arr[newy][x] == '.':
          arr[y][x] = 'X'
          arr[newy][x] = 'D'    
          movement = True
  for y in range(rows):
    for x in range(cols):
      if arr[y][x] == 'D':
        arr[y][x] = 'v'
      elif arr[y][x] == 'X':
        arr[y][x] = '.'
  if not movement:
    print(str(i+1))
    break
    


#print_ocean(arr)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')