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
for s in l:
  arr = s.split(',')
  x = int(arr[0])
  y = int(arr[1])
  z = int(arr[2])
  lava.add((x,y,z))

count = 0
for p in lava:
  (x,y,z) = p
  arr = adjLava(x,y,z)
  for p2 in arr:
    (x1,y1,z1) = p2
    if not (x1,y1,z1) in lava:
      count += 1
print(count)








print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')