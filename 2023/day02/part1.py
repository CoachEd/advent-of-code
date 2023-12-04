# Day 2 Part 1
import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')
 
# SOLUTION
# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  line = line.strip()
  l.append(line)

d = {} # n : [r, g, b]
for s in l:
  a1 = s.split(':')
  n = int(a1[0].replace('Game ',''))
  r0 = -1
  g0 = -1
  b0 = -1
  reaches = a1[1].split(';')
  for r in reaches:
    cubes = r.split(',')
    for c in cubes:
      c = c.lstrip()
      count = c.split(' ')
      c0 = int(count[0])
      color = count[1]
      if color == 'red':
        r0 = c0 if c0 > r0 else r0
      elif color == 'green':
        g0 = c0 if c0 > g0 else g0
      elif color == 'blue':
        b0 = c0 if c0 > b0 else b0
  d[n] = [r0,g0,b0]
 
# main
# 12 red cubes, 13 green cubes, and 14 blue cubes

tot = 0
for k,v in d.items():
  if v[0] > 12 or v[1] > 13 or v[2] > 14:
    # impossible
    pass
  else:
    tot += k
print(tot)




print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')