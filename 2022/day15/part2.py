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
row = 10 # TODO: INPUT
#row = 2000000 # TODO: INPUT
xs = set()
for i in range(len(sensors)):
  (sx,sy) = sensors[i]
  (bx,by) = beacons[i]
  dist = abs(sx-bx) + abs(sy-by)
  min_y = sy - dist
  max_y = sy + dist
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
      xs.add(i)

    # remove sensors
    for (x,y) in sensors:
      if x >= start_x and x <= end_x and y == row:
        if x in xs:
          xs.remove(x)

    # remove beacons
    for (x,y) in beacons:
      if x >= start_x and x <= end_x and y == row:
        if x in xs:
          xs.remove(x)


print(len(xs))
# 6262636 TOO HIGH
# 9584037
# 5108096 YES!


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')