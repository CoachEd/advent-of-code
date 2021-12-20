"""
AoC
"""
import time
import sys
from copy import copy, deepcopy
import math

def count_lights(m,offset_y,offset_x):
  n = 0
  (min_row,min_col,max_row,max_col) = get_bounds(m)
  for y in range(min_row+offset_y,max_row-offset_y):
    for x in range(min_col+offset_x,max_col-offset_x):
      c = m[y][x]
      if c == '#':
        n += 1
  return n

def get_bounds(m):
  max_row = -1
  max_col = -1
  min_row = sys.maxsize
  min_col = sys.maxsize
  for y in range(len(m)):
    for x in range(len(m[y])):
      if m[y][x] == '#':
        if y > max_row:
          max_row = y
        if x > max_col:
          max_col = x
        if y < min_row:
          min_row = y
        if x < min_col:
          min_col = x
  return (min_row-1,min_col-1,max_row+1,max_col+1)

def print_m(m):
  (min_row, min_col, max_row, max_col) = get_bounds(m)
  s = ''
  for y in range(min_row,max_row+1):
    for x in range(min_col,max_col+1):
      s += m[y][x]
    s += '\n'
  print(s)

start_secs = time.time()

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

alg = l[0]
del l[0]
del l[0]

rmult = 4
cmult = 4
num_rows = len(l) * rmult
num_cols = len(l[0]) * cmult

m = [ [ '.' for r in range(num_rows) ] for c in range(num_cols) ]
midy = math.floor(num_rows / 2) - math.floor(len(l)/2)
midx = math.floor(num_cols / 2) - math.floor(len(l[0])/2)

y = midy
for r in l:
  x = midx
  for c in r:
    m[y][x] = c
    x += 1
  y += 1

# main
reps = 2
for i in range(reps):
  m1 = deepcopy(m)
  (min_row,min_col,max_row,max_col) = get_bounds(m)
  for y in range(min_row-6,max_row+6):
    for x in range(min_col-6,max_col+6):
      s =  m[y-1][x-1] + m[y-1][x] +  m[y-1][x+1]
      s += m[y][x-1]   + m[y][x]   + m[y][x+1]
      s += m[y+1][x-1] + m[y+1][x] + m[y+1][x+1]
      n = int(s.replace('.','0').replace('#','1'),2)
      m1[y][x] = alg[n]
  m = deepcopy(m1)
  
print_m(m)

# do not count frame around output...
print( count_lights(m,9,9) )

# 5255 too high
# 5228 too high
# 5225 - CORRECT!!!s
# 5157 incorrect
# 5039 incorrect

end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
