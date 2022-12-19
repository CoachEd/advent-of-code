import time
import sys
from copy import copy, deepcopy
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
space = set()

#row = 2000000 # TODO: INPUT
xs = set()
for i in range(len(sensors)):
  (sx,sy) = sensors[i]
  (bx,by) = beacons[i]
  dist = abs(sx-bx) + abs(sy-by)
  min_y = sy - dist
  max_y = sy + dist
  for row in range(bound_max+1):
    if row >= min_y and row <= max_y:
      # consider this sensor
      d2 = abs(row) - abs(sy)
      if row < sy:
        d2 = abs(sy) - abs(row)

      lx = sx - dist + d2
      rx = sx + dist - d2

      start_x = lx
      end_x = rx
      for i in range(start_x, end_x + 1):
        if i >= bound_min and i <= bound_max:
          space.add( (i, row) )

done = False
for y in range(bound_max+1):
  for x in range(bound_max+1):
    if not (x,y) in space:
      print( x * 4000000 + y)
      done = True
      break
  if done:
    break


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')