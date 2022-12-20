import time
import sys
from copy import copy, deepcopy
from sympy import Interval, Union
import numpy as np
start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

# main
sensors = []
beacons = []

# Sensor at x=2, y=18: closest beacon is at x=-2, y=15
for s in l:
  s2 = s.replace(',','').replace(':','').replace('x=','').replace('y=','').replace('Sensor at','').replace('closest beacon is at','').replace('  ',' ').strip()
  a = s2.split()
  sx = int(a[0])
  sy = int(a[1])
  bx = int(a[2])
  by = int(a[3])
  sensors.append((sx,sy))
  beacons.append((bx,by))

# for each sensor, calculate its areas
bound_max = 20
#bound_max = 4000000
xs = set()
ranges = dict()
for i in range(len(sensors)):
  (sx,sy) = sensors[i]
  (bx,by) = beacons[i]
  dist = abs(sx-bx) + abs(sy-by)
  min_y = sy - dist
  max_y = sy + dist
  for row in range(min_y,max_y+1):
    if row >= min_y and row <= max_y:
      # consider this sensor
      d2 = abs(row) - abs(sy)
      if row < sy:
        d2 = abs(sy) - abs(row)

      lx = sx - dist + d2
      rx = sx + dist - d2

      if row < 0 or row > bound_max:
        continue

      if not row in ranges:
        ranges[row] = []
      start_x = lx
      end_x = rx
      ranges[row].append((start_x, end_x))

# add sensors and beacons
for (x,y) in sensors:
  if y >= 0 and y <= bound_max:
    ranges[y].append((x,x))
for (x,y) in beacons:
  if y >= 0 and y <= bound_max:
    ranges[y].append((x,x))

for r in range(0, bound_max+1):
  a = ranges[r]
  b = []
  for begin,end in sorted(a):
    if b and b[-1][1] >= begin - 1:
      b[-1][1] = max(b[-1][1], end)
    else:
      b.append([begin, end])
  b = list(map(tuple, b))
  num_taken = 0
  for (x,y) in b:
    if x < 0 and y < 0:
      continue
    if x > bound_max and y > bound_max:
      continue
    if y < 0:
      continue  
    if x > bound_max:
      continue

    if x < 0:
      x = 0
    if y > bound_max:
      y = bound_max    
    num_taken += (y - x) + 1

  #print(str(r) + ': ' + str(num_taken))
  if num_taken == bound_max:
    # found the row    
    arr0 = np.array([' ']*(bound_max+1))
    for (x,y) in ranges[r]:
      if x < 0:
        x = 0
      if y > bound_max:
        y = bound_max
      arr0[x:y+1] = '#'
    for x in range(len(arr0)):
      if arr0[x] == ' ':
        print(x*4000000+r)



print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')