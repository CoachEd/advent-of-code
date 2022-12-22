import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

def addPockets(x,y,z,pockets):
  global min_x, min_y, min_z, max_x, max_y, max_z, lava

  if x < min_x or y < min_y or z < min_z or x > max_x or y > max_y or z > max_z:
    # reached infinity
    return False
  
  if (x,y,z) in lava:
    return False

  arr = adjLava(x,y,z)
  new_pockets = set()
  for (x1,y1,z1) in arr:
    if not (x1,y1,z1) in pockets and not (x1,y1,z1) in lava:
      new_pockets.add((x1,y1,z1))

  if len(new_pockets) == 0:
    # no new pockets can be added
    return True
  
  isPocket = True
  pockets.update(new_pockets)
  for (x0,y0,z0) in new_pockets:
    if (x0,y0,z0) not in lava:
      isPocket = isPocket and addPockets(x0,y0,z0,pockets.copy())

  return isPocket

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
pockets = set()
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
  min_x = min(min_x, x)
  min_y = min(min_y, y)
  min_z = min(min_z, z)
  max_x = max(max_x, x)
  max_y = max(max_y, y)
  max_z = max(max_z, z)

count = 0
for p in lava:
  (x,y,z) = p
  arr = adjLava(x,y,z)
  for p2 in arr:
    (x1,y1,z1) = p2
    if not (x1,y1,z1) in lava:
      count += 1

pocket_faces = 0
for p in lava:
  (x,y,z) = p
  arr = adjLava(x,y,z)
  for (x1,y1,z1) in arr:
    # see if this face is inside a pocket
    pockets = set()
    if addPockets(x1,y1,z1,pockets):
      pocket_faces += 1

print(str(count - pocket_faces))
# 1496 TOO LOW
# 3464 TOO HIGH


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')