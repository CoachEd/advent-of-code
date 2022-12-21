import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

def adjLava(x,y,z):
  return [
    (x,y-1,z),
    (x,y+1,z),
    (x-1,y,z),
    (x+1,y,z),
    (x,y,z-1),
    (x,y,z+1)
  ]

# SOLUTION
# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

lava = set()
min_x = float('inf')
min_y = float('inf')
min_z = float('inf')
max_x = float('-inf')
max_y = float('-inf')
max_z = float('-inf')

for s in l:
  arr = s.split(',')
  x = int(arr[0])
  y = int(arr[1])
  z = int(arr[2])
  lava.add((x,y,z))
  min_x = min(min_x, x) - 1
  min_y = min(min_y, y) - 1
  min_z = min(min_z, z) - 1
  max_x = max(max_x, x) + 1
  max_y = max(max_y, y) + 1
  max_z = max(max_z, z) + 1

air = set()
for x in range(min_x, max_x+1):
  for y in range(min_y, max_y+1):
    for z in range(min_z, max_z+1):
      if not (x,y,z) in lava:
        air.add((x,y,z))

count = 0
for p in lava:
  (x,y,z) = p
  arr = adjLava(x,y,z)
  for p2 in arr:
    (x1,y1,z1) = p2
    if not (x1,y1,z1) in lava:
      count += 1

count2 = 0
for p in air:
  (x,y,z) = p
  arr = adjLava(x,y,z)
  air_pocket = True
  for p2 in arr:
    (x1,y1,z1) = p2
    if not (x1,y1,z1) in lava:
      air_pocket = False
      break
  if air_pocket:
    count2 += 1
    #print((x,y,z))


print(str(count - (count2 * 6)))
# 1496 TOO LOW
# 


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')