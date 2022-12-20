import time
import sys
from copy import copy, deepcopy
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
bound_min = 0
#bound_max = 4000000
bound_max = 20
row_bounds = dict()

xs = set()
for i in range(len(sensors)):
  (sx,sy) = sensors[i]
  (bx,by) = beacons[i]
  dist = abs(sx-bx) + abs(sy-by)
  min_y = sy - dist
  max_y = sy + dist
  print('sensor %s' % str(i))
  for row in range(min_y,max_y+1):
    if not row in row_bounds:
      row_bounds[row] = []
    if row >= 0 and row <= bound_max:
      d2 = abs(row) - abs(sy)
      if row < sy:
        d2 = abs(sy) - abs(row)

      lx = sx - dist + d2
      rx = sx + dist - d2
      if rx < bound_min or lx > bound_max:
        # skip this sensor
        break

      start_x = lx
      end_x = rx
      #print('sensor ' + str(i) + '    ' + str((start_x,end_x)) + ' ' + str(row))
      row_bounds[row].append((start_x,end_x))
      #for k in range(start_x, end_x + 1):
      #  if k >= bound_min and k <= bound_max:
          
          #space.add( (k, row) )

print()

# add beacons and sensors
for (x,y) in beacons:
  if y >=0 and y <= bound_max:
    row_bounds[y].append((x,x))
for (x,y) in sensors:
  if y >=0 and y <= bound_max:
    row_bounds[y].append((x,x))

for r in range(len(row_bounds)):
  a = row_bounds[r]
  b = []
  print(r)
  print(sorted(a))
  for begin,end in sorted(a):
    if b and b[-1][1] >= begin - 1:
      b[-1] = (b[-1][0], end)
    else:
      b.append((begin, end))
  print(b)
  print()
  row_bounds[r] = deepcopy(b)

arr0 = np.array([' ']*(bound_max+1))
#for row in range(len(row_bounds)-1, -1, -1):
start_row = 0
end_row = 20
for row in range(start_row,end_row+1):
  print('row ' + str(row))
  arr0.fill(' ')
  for rng in row_bounds[row]:
    (x0,x1) = rng
    if x0 < 0:
      x0 = 0
    if x1 > bound_max:
      x1 = bound_max
    arr0[x0:x1+1] = '#'
    #for x2 in range(x0,x1+1):
    #  if x2 >= 0 and x2 <= bound_max:
    #    arr0[x2] = '#'
  #print(arr0)
  (unique) = np.unique(arr0, return_counts=False)
  #print(unique)
  #print(len(unique))
  #d = dict(zip(unique, counts))
  #print('row: ' + str(row) + ' counts: ' + str(d))
  #if ' ' in d:
  if len(unique) == 2:
    #print('row ' + str(row) + '   ' + str(d))
    for x in range(0, bound_max+1):
      if arr0[x] == ' ':
        print((x * 4000000 + row))
        exit()
  

"""
done = False
for y in range(bound_max+1):
  for x in range(bound_max+1):
    if not (x,y) in space:
      print( x * 4000000 + y)
      done = True
      break
  if done:
    break
"""

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')