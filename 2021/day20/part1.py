"""
AoC
"""
import time
import sys
from copy import copy, deepcopy
import math

def remove_ring(m):
  for y in range(len(m)):
    for x in range(len(m[y])):
      if y == 1 or y == len(m)-2 or x == 1 or x == len(m[y])-2:
        m[y][x] = '.'

def get_bounds(m):
  minx = sys.maxsize
  miny = sys.maxsize
  maxx = -1
  maxy = -1
  for y in range(len(m)):
    for x in range(len(m[y])):
      if m[y][x] == '#':
        if y < miny:
          miny = y
        if x < minx:
          minx = x
        if y > maxy:
          maxy = y
        if x > maxx:
          maxx = x
  return (minx,miny,maxx,maxy)

def count_lights(m):
  n = 0
  for y in range(len(m)):
    for x in range(len(m[y])):
      c = m[y][x]
      if c == '#':
        n += 1
  return n

def print_m(m):
  s = ''
  for row in m:
    for c in row:
      s += c
    s += '\n'
  print(s)

def pad_sides(m):
  # padding length 2 on all sides
  padding = 5
  min_y = sys.maxsize
  max_y = -1
  min_x = sys.maxsize
  max_x = -1
  for y in range(len(m)):
    for x in range(len(m[y])):
      if m[y][x] == '#':
        if y < min_y:
          min_y = y
        if x < min_x:
          min_x = x
        if x > max_x:
          max_x = x
        if y > max_y:
          max_y = y

  m2 = [ ['.' for x in range(max_x-min_x+1)] for y in range(max_y-min_y+1) ]
  y0 = 0
  for y in range(min_y,max_y+1):
    x0 = 0
    for x in range(min_x,max_x+1):
      m2[y0][x0] = m[y][x]
      x0 += 1
    y0 += 1
      
  for row in m2:
    for i in range(padding):
      row.insert(0,'.')
      row.append('.')
  mrow = ['.' for x in range(len(m2[0])) ]
  for i in range(padding):
    m2.insert(0,mrow.copy())
    m2.append(mrow.copy())
  
  return m2

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

m = [ [ '.' for r in range(len(l)) ] for c in range(len(l[0])) ]
for y in range(len(l)):
  for x in range(len(l[y])):
    m[y][x] = l[y][x]

m = pad_sides(m)

# main
reps = 2
#print_m(m)
for i in range(reps):
  m1 = deepcopy(m)
  for y in range(len(m1)):
    for x in range(len(m1[y])):
      # skip first and last rows, first and last columns
      if y == 0 or x == 0 or y == len(m1)-1 or x == len(m1[0])-1:
        continue

      s =  m[y-1][x-1] + m[y-1][x] +  m[y-1][x+1]
      s += m[y][x-1]   + m[y][x]   + m[y][x+1]
      s += m[y+1][x-1] + m[y+1][x] + m[y+1][x+1]
      n = int(s.replace('.','0').replace('#','1'),2)
      m1[y][x] = alg[n]
  m = deepcopy(m1)


  if i % 2 != 0:
    print_m(m)
    # remove ring 7 off top and bottom, 6 off right and left
    for i in range(7):
      del m[0]
      del m[-1]
    for row in m:
      for i in range(6):
        del row[0]
        del row[-1]
  
  # pad
  m = pad_sides(m)
  print_m(m)

print( count_lights(m) )
# sample input
# print( count_lights(m,0,0) )

# actual input: do not count frame around output...
#print( count_lights(m,9,9) )

# 241683 too high
# 19999 too high
# 19486 wrong
# pad 1: 4780
# pad 2: 19486
# pad 3: 42398
# pad 4: 68555
# pad 5: 109538
# pad 6: 
# wrong: 16739

# TODO: 752 x 752
# TODO: try setting color 000000000 to ' ' to skip it? add logic to skip it?

end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
