import sys
import time
import math
from copy import copy, deepcopy

"""
import cProfile, pstats
from io import StringIO
pr = cProfile.Profile()  # create a profile object
pr.enable()  # start profiling
"""


def applyGravity(x1,x2,vx1,vx2):
  if alldata[x1] < alldata[x2]:
    alldata[vx1] = alldata[vx1] + 1
    alldata[vx2] = alldata[vx2] - 1
  elif alldata[x1] > alldata[x2]:
    alldata[vx1] = alldata[vx1] - 1
    alldata[vx2] = alldata[vx2] + 1  

def updatePositions(x1,y1,z1,vx1,vy1,vz1):
  alldata[x1] = alldata[x1] + alldata[vx1]
  alldata[y1] = alldata[y1] + alldata[vy1]
  alldata[z1] = alldata[z1] + alldata[vz1]

def sumPlanet(x1,y1,z1,vx1,vy1,vz1):
  sum1 = abs(alldata[x1]) + abs(alldata[y1]) + abs(alldata[z1])
  sum2 = abs(alldata[vx1]) + abs(alldata[vy1]) + abs(alldata[vz1])
  return (sum1 * sum2)

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

alldata = []
index = 0
for r in tarr:
  x = r.split(',')
  for n in x:
    alldata.append(int(n))
  alldata.extend([0,0,0])

checkarr = []
"""
To apply gravity, consider every pair of moons. 
On each axis (x, y, and z), the velocity of each moon changes by exactly +1 or -1 to pull the moons together. 
For example, if Ganymede has an x position of 3, and Callisto has a x position of 5, 
then Ganymede's x velocity changes by +1 (because 5 > 3) and Callisto's x velocity changes by -1 (because 3 < 5). 
However, if the positions on a given axis are the same, the velocity on that axis does not change for that pair of moons.


 0  1   2   3   4   5   6   7   8    9  10  11   12  13  14 15  16  17  18  19 20  21  22  23
 x1 y1 z1  vx1 vy1 vz1  x2  y2  z2  vx2 vy2 vz2  x3  y3  z3 vx3 vy3 vz3 x4  y4 z4  vx4 vy4 vz4
[3, 2, -6,  0,  0,  0, -13, 18, 10,  0,  0,  0,  -8, -1, 13, 0,  0,  0,  5, 10, 4,  0,  0,  0]

"""

x1=0
y1=1
z1=2
vx1=3
vy1=4
vz1=5

x2=6
y2=7
z2=8
vx2=9
vy2=10
vz2=11

x3=12
y3=13
z3=14
vx3=15
vy3=16
vz3=17

x4=18
y4=19
z4=20
vx4=21
vy4=22
vz4=23

s = ''
s1 = ''
t = 0

while True:
  t = t + 1
  # steps 1 to steps

  # apply gravity to velocity

  # x1 to x2
  applyGravity(x1,x2,vx1,vx2)
  applyGravity(y1,y2,vy1,vy2)
  applyGravity(z1,z2,vz1,vz2)

  # x1 to x3
  applyGravity(x1,x3,vx1,vx3)
  applyGravity(y1,y3,vy1,vy3)
  applyGravity(z1,z3,vz1,vz3)

  # x1 to x4
  applyGravity(x1,x4,vx1,vx4)
  applyGravity(y1,y4,vy1,vy4)
  applyGravity(z1,z4,vz1,vz4)

  # x2 to x3
  applyGravity(x2,x3,vx2,vx3)
  applyGravity(y2,y3,vy2,vy3)
  applyGravity(z2,z3,vz2,vz3)

  # x2 to x4
  applyGravity(x2,x4,vx2,vx4)
  applyGravity(y2,y4,vy2,vy4)
  applyGravity(z2,z4,vz2,vz4)

  # x3 to x4
  applyGravity(x3,x4,vx3,vx4)
  applyGravity(y3,y4,vy3,vy4)
  applyGravity(z3,z4,vz3,vz4)

  updatePositions(x1,y1,z1,vx1,vy1,vz1)
  updatePositions(x2,y2,z2,vx2,vy2,vz2)
  updatePositions(x3,y3,z3,vx3,vy3,vz3)
  updatePositions(x4,y4,z4,vx4,vy4,vz4)

  
  
  key = str(alldata[18])+','+str(alldata[19])+','+str(alldata[20]) # 1  
  if key in alldata:
    #print('t' + str(t) + ': ' + key)
    key = key + '|' + str(alldata[6])+','+str(alldata[7])+','+str(alldata[8]) + '|' + str(alldata[0])+','+str(alldata[1])+','+str(alldata[2]) + '|' + str(alldata[12])+','+str(alldata[13])+','+str(alldata[14])
    if key in alldata:
      print('t' + str(t) + ': ' + str(alldata))
    else:
      alldata.append(key)
  else:
    alldata.append(key)
  """
  totenergy = 0
  totenergy = totenergy + sumPlanet(x1,y1,z1,vx1,vy1,vz1)
  totenergy = totenergy + sumPlanet(x2,y2,z2,vx2,vy2,vz2)
  totenergy = totenergy + sumPlanet(x3,y3,z3,vx3,vy3,vz3)
  totenergy = totenergy + sumPlanet(x4,y4,z4,vx4,vy4,vz4)

  stemp = str(alldata)
  if str(totenergy) in s:
    if stemp in s1:
      print('t' + str(t) + ' done.')
      break
    else:
      s1 = s1 + '|' + stemp
  else:
    s = s + '|' + str(totenergy)
  """


  if t == 1000000:
    break


"""
pr.disable()  # end profiling

# print out some stats.
s = StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
"""

#print(totenergy)

end_secs = time.time()
print('elapsed time: ' + str(end_secs - start_secs) + ' seconds')
