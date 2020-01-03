import sys
import time
import math
from copy import copy, deepcopy

start_secs = time.time()

gravs = [3, 1, -1, -3]
inp1 = """<x=3, y=2, z=-6>
<x=-13, y=18, z=10>
<x=-8, y=-1, z=13>
<x=5, y=10, z=4>
"""
inp1 = inp1.replace("<x=", "")
inp1 = inp1.replace("y=", "")
inp1 = inp1.replace("z=", "")
inp1 = inp1.replace(">", "")
inp1 = inp1.replace(" ","")
tarr = inp1.split('\n')[:-1]
posarr = []
for r in tarr:
  x = r.split(',')
  temp = []
  temp2 = []
  for n in x:
    temp.append(int(n))
    temp2.append(0)

  posarr.append(temp + temp2)






"""
To apply gravity, consider every pair of moons. 
On each axis (x, y, and z), the velocity of each moon changes by exactly +1 or -1 to pull the moons together. 
For example, if Ganymede has an x position of 3, and Callisto has a x position of 5, 
then Ganymede's x velocity changes by +1 (because 5 > 3) and Callisto's x velocity changes by -1 (because 3 < 5). 
However, if the positions on a given axis are the same, the velocity on that axis does not change for that pair of moons.
"""
steps = 1000
for t in range(1,steps+1):
  # steps 1 to steps

  # apply gravity to velocity
  # sort by 0, 1, 2
  # 3, 1, -1, -3

  # apply gravity
  for i in range(4):
    posarr.sort(key = lambda x: x[2])
    for p in range(4):
      posarr[p][i+3] = posarr[p][i+3] + gravs[i]

  # move planets
  for p in posarr:
    for i in range(3):
      p[i] = p[i] + p[i+3]





totenergy = 0
for p in posarr:
  kinenergy = 0
  potenergy = 0
  for i in range(3):
    potenergy = potenergy + abs(p[i])
  for i in range(3,6):
    kinenergy = kinenergy + abs(p[i])

  totenergy = totenergy + (kinenergy * potenergy)

print(totenergy)


end_secs = time.time()
print('elapsed time: ' + str(end_secs - start_secs) + ' seconds')
