import time
import sys
from copy import copy, deepcopy
import numpy as np
start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp2.txt", "r", encoding='utf-8')
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
  for row in range(bound_max+1):
    if not row in row_bounds:
      row_bounds[row] = []
    if row >= min_y and row <= max_y:
      # consider this sensor
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
for row in range(len(row_bounds)-1, -1, -1):
  #print('row ' + str(row))
  arr = row_bounds[row]
  arr.sort()
  b = []

  for begin,end in arr:
    if b and b[-1][1] >= begin - 1:
      b[-1] = (b[-1][0], end)
    else:
      b.append((begin, end))  
    if len(b) == 2:
      (x0,x1) = b[0]
      (x2,x3) = b[1]
      if (x2 - x1) == 2 and not (x2-1,row) in sensors and not (x2-1,row) in beacons and (x2-1) >=0 and (x2-1) <= bound_max:
        print('HERE')
        print(((x2-1) * 4000000 + row))

  """
  for k in range(len(arr)-1):
    rng = arr[k]
    rng2 = arr[k+1]
    (x0,x1) = rng
    (x2,x3) = rng2


    if k == 0 and x0 == 1:
      # found gap
      print('HERE"')
      print( 0  * 4000000 + row)
    elif x2 == (x1 + 2) and not (x2-1,row) in sensors and not (x2-1,row) in beacons and (x2-1) <= bound_max and (x2-1) >= 0 and ((x2-1) >= 0 and (x2-1) <= bound_max):
      # found gap
      print()
      print(x2-1, row)
      print(((x2-1) * 4000000 + row))
      exit()
  """
  
# 10954487965884 TOO  HIGH
# 1014985807485  TOO LOW
# 
# 

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