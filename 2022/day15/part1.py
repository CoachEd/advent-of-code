import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

def getArea(sx,sy,bx,by):
  dist = abs((sx-bx)) + abs((sy-by))
  points = []

  # float('-inf') smallest number in Python
  # float('+inf') largest number in Python

  min_x = sx - dist
  max_x = sx + dist
  min_y = sy - dist
  max_y = sy + dist

  # add points left and right of sensor
  lx = sx - 1
  rx = sx + 1
  for i in range(dist):
    points.append((lx,sy))
    points.append((rx,sy))
    lx -= 1
    rx += 1

  # add points top and bottom of sensor
  uy = sy - 1
  dy = sy + 1
  d2 = dist - 1
  for i in range(dist):
    points.append((sx,uy))
    points.append((sx,dy))

    lx = sx - 1
    rx = sx + 1
    for i in range(d2):
      points.append((lx,uy))
      points.append((rx,uy))
      points.append((lx,dy))
      points.append((rx,dy))      
      lx -= 1
      rx += 1
    uy -= 1
    dy += 1
    d2 -= 1

  # remove beacon from the list
  points.remove((bx,by))
  return (points, min_x, max_x, min_y, max_y)



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
positions = 0
seen = []
row = 10 # TODO: INPUT
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
    count = abs(end_x - start_x) + 1
    
    # remove sensors
    for (x,y) in sensors:
      if x >= start_x and x <= end_x and y == row:
        count -= 1
    
    # remove beacons
    for (x,y) in beacons:
      if x >= start_x and x <= end_x and y == row:
        count -= 1

    positions += count

print(positions)
# 6262636 TOO HIGH
# 9584037


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')