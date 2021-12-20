"""
AoC
"""
import time
import sys
from copy import copy, deepcopy
from numpy import rot90, array

def rotations24(polycube):
    """List all 24 rotations of the given 3d array"""
    def rotations4(polycube, axes):
        """List the four rotations of the given 3d array in the plane spanned by the given axes."""
        for i in range(4):
             yield rot90(polycube, i, axes)

    # imagine shape is pointing in axis 0 (up)

    # 4 rotations about axis 0
    yield from rotations4(polycube, (1,2))

    # rotate 180 about axis 1, now shape is pointing down in axis 0
    # 4 rotations about axis 0
    yield from rotations4(rot90(polycube, 2, axes=(0,2)), (1,2))

    # rotate 90 or 270 about axis 1, now shape is pointing in axis 2
    # 8 rotations about axis 2
    yield from rotations4(rot90(polycube, axes=(0,2)), (0,1))
    yield from rotations4(rot90(polycube, -1, axes=(0,2)), (0,1))

    # rotate about axis 2, now shape is pointing in axis 1
    # 8 rotations about axis 1
    yield from rotations4(rot90(polycube, axes=(0,1)), (0,2))
    yield from rotations4(rot90(polycube, -1, axes=(0,1)), (0,2))

start_secs = time.time()
print('')

# read in input file
d=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
scanner_num = 0
points = []
for line in lines:
  # --- scanner 0 ---
  s = line.strip()
  if s.startswith('---'):
    continue
  if len(s) == 0:
    d.append(points)
    points = []
    scanner_num += 1
    continue
  arr = [ int(x) for x in s.split(',')]
  points.append(arr)
d.append(points)
  
# d is an array of scanners data; each scanner's data is an array of point x,y,z
print(d)


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
