"""
AoC
"""
import time
import sys
from copy import copy, deepcopy
import math

def valid(y,x,m):
  if y < 0 or x < 0 or y >= len(m) or x >= len(m[0]):
    return False
  return True


def count_lights(m):
  n = 0
  for y in range(len(m)):
    for x in range(len(m[y])):
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
  s = ''
  for row in m:
    for c in row:
      s += c
    s += '\n'
  print(s)

start_secs = time.time()

# read in input file
l=[]
my_file = open("inp_sample.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

alg = l[0]
del l[0]
del l[0]


#num_rows = 100
#num_cols = 100
num_rows = 5
num_cols = 5


m = [ [ '.' for r in range(num_rows) ] for c in range(num_cols) ]
for y in range(len(m)):
  for x in range(len(m[y])):
    m[y][x] = l[y][x]


# make m 2 bigger on each edge
offset = 2
ROWS = num_rows+offset*2
COLS = num_cols+offset*2
m2 = [ [ '.' for r in range(ROWS) ] for c in range(COLS) ]
for y in range(len(m)):
  for x in range(len(m[y])):
    m2[y+offset][x+offset]=m[y][x]

# main
reps = 50
print_m(m2)
for i in range(reps):
  m1 = deepcopy(m2)
  for y in range(len(m2)):
    for x in range(len(m2[y])):
      
      # skip first and last rows, first and last columns
      if y == 0 or x == 0 or y == len(m2)-1 or x == len(m2[0])-1:
        continue

      s =  m2[y-1][x-1] + m2[y-1][x] +  m2[y-1][x+1]
      s += m2[y][x-1]   + m2[y][x]   + m2[y][x+1]
      s += m2[y+1][x-1] + m2[y+1][x] + m2[y+1][x+1]
      n = int(s.replace('.','0').replace('#','1'),2)
      m1[y][x] = alg[n]
  m2 = deepcopy(m1)
  
  ROWS = ROWS + 2
  COLS = COLS + 2
  offset = 1
  m3 = [ [ '.' for r in range(ROWS) ] for c in range(COLS) ]
  for y in range(len(m2)):
    for x in range(len(m2[y])):
      m3[y+offset][x+offset]=m2[y][x]
  m2 = deepcopy(m3)
  
  
  print_m(m2)
  
print_m(m2)
print( count_lights(m2) )
# sample input
# print( count_lights(m,0,0) )

# actual input: do not count frame around output...
#print( count_lights(m,9,9) )

# 241683 too high
# 19999 too high

# TODO: 752 x 752
# TODO: try setting color 000000000 to ' ' to skip it? add logic to skip it?

end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
