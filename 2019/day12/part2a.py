import sys
import time
import math
from copy import copy, deepcopy

def tot_energy(p,v):
  totenergy = 0
  for i in range(0,len(p)):
    kinenergy = 0
    potenergy = 0
    for j in range(0,len(p[i])):
      kinenergy = kinenergy + abs(v[i][j])
      potenergy = potenergy + abs(p[i][j])
    totenergy = totenergy + (kinenergy * potenergy)
  return totenergy

ens = set()
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
steps = 999999999999999
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

      #if x1 < x2:
      #  velarr[i][0] = velarr[i][0] + 1
      #  velarr[j][0] = velarr[j][0] - 1
      #elif x2 < x1:
      #  velarr[i][0] = velarr[i][0] - 1
      #  velarr[j][0] = velarr[j][0] + 1        
      a1 = x1 - x2
      a2 = a1 - .01
      try:
        change = math.floor(a1 / abs(a1)) * -1
      except:
        change = 0
      velarr[i][0] = velarr[i][0] + change
      velarr[j][0] = velarr[j][0] - change



      #if y1 < y2:
      #  velarr[i][1] = velarr[i][1] + 1
      #  velarr[j][1] = velarr[j][1] - 1
      #elif y2 < y1:
      #  velarr[i][1] = velarr[i][1] - 1
      #  velarr[j][1] = velarr[j][1] + 1
      a1 = y1 - y2
      a2 = a1 - .01
      try:
        change = math.floor(a1 / abs(a1)) * -1
      except:
        change = 0
      velarr[i][1] = velarr[i][1] + change
      velarr[j][1] = velarr[j][1] - change  



  
      #if z1 < z2:
      #  velarr[i][2] = velarr[i][2] + 1
      #  velarr[j][2] = velarr[j][2] - 1
      #elif z2 < z1:
      #  velarr[i][2] = velarr[i][2] - 1
      #  velarr[j][2] = velarr[j][2] + 1
      a1 = z1 - z2
      a2 = a1 - .01
      try:
        change = math.floor(a1 / abs(a1)) * -1
      except:
        change = 0
      velarr[i][2] = velarr[i][2] + change
      velarr[j][2] = velarr[j][2] - change          

  for i in range(0,len(posarr)):
    for j in range(0,len(posarr[i])):
      posarr[i][j] = posarr[i][j] + velarr[i][j]

  #energy = tot_energy(posarr,velarr) 
  #if energy in ens:
  #  print()
  #  print('found')
  #  print(t)
  #  print(posarr)
  #  print(velarr)
  #  print()
  #  sys.exit()
  #else:
  #  ens.add(energy)
  
  s = '{0}{1}{2}{3}{4}{5} {6}{7}{8}{9}{10}{11}  {12}{13}{14}{15}{16}{17}  {18}{19}{20}{21}{22}{23}'.format(posarr[0][0],posarr[0][1],posarr[0][2],velarr[0][0],velarr[0][1],velarr[0][2] , posarr[1][0],posarr[1][1],posarr[1][2],velarr[1][0],velarr[1][1],velarr[1][2], posarr[2][0],posarr[2][1],posarr[2][2],velarr[2][0],velarr[2][1],velarr[2][2] , posarr[3][0],posarr[3][1],posarr[3][2],velarr[3][0],velarr[3][1],velarr[3][2] )
  
  #s = ''.join(str(e) for e in posarr[0])
  #s = s + ''.join(str(e) for e in velarr[0])
  
  if s in ens:
    print('found')
    print(t-1)
    sys.exit()
  else:
    ens.add(s)  

# output
for m in posarr:
  print(str(m[0]) + ',' + str(m[1]) + ',' + str(m[2]))
print()

for m in velarr:
  print(str(m[0]) + ',' + str(m[1]) + ',' + str(m[2]))






end_secs = time.time()
print('elapsed time: ' + str(end_secs - start_secs) + ' seconds')
