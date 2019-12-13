import sys
import time
import math
from copy import copy, deepcopy

start_secs = time.time()

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
velarr = []
for r in tarr:
  x = r.split(',')
  temp = []
  temp2 = []
  for n in x:
    temp.append(int(n))
    temp2.append(0)
  posarr.append(temp)
  velarr.append(temp2)






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
  for i in range(0,len(velarr)-1):
    for j in range(i+1,len(velarr)):
      x1 = posarr[i][0]
      y1 = posarr[i][1]
      z1 = posarr[i][2]
      x2 = posarr[j][0]
      y2 = posarr[j][1]
      z2 = posarr[j][2]

      if x1 < x2:
        velarr[i][0] = velarr[i][0] + 1
        velarr[j][0] = velarr[j][0] - 1
      elif x2 < x1:
        velarr[i][0] = velarr[i][0] - 1
        velarr[j][0] = velarr[j][0] + 1        

      if y1 < y2:
        velarr[i][1] = velarr[i][1] + 1
        velarr[j][1] = velarr[j][1] - 1
      elif y2 < y1:
        velarr[i][1] = velarr[i][1] - 1
        velarr[j][1] = velarr[j][1] + 1
  
      if z1 < z2:
        velarr[i][2] = velarr[i][2] + 1
        velarr[j][2] = velarr[j][2] - 1
      elif z2 < z1:
        velarr[i][2] = velarr[i][2] - 1
        velarr[j][2] = velarr[j][2] + 1

  for i in range(0,len(posarr)):
    for j in range(0,len(posarr[i])):
      posarr[i][j] = posarr[i][j] + velarr[i][j]

# output
for m in posarr:
  print(str(m[0]) + ',' + str(m[1]) + ',' + str(m[2]))
print()

for m in velarr:
  print(str(m[0]) + ',' + str(m[1]) + ',' + str(m[2]))


totenergy = 0
for i in range(0,len(posarr)):
  kinenergy = 0
  potenergy = 0
  for j in range(0,len(posarr[i])):
    kinenergy = kinenergy + abs(velarr[i][j])
    potenergy = potenergy + abs(posarr[i][j])
  totenergy = totenergy + (kinenergy * potenergy)


print(totenergy)


end_secs = time.time()
print('elapsed time: ' + str(end_secs - start_secs) + ' seconds')
