import sys
import time
import math
from copy import copy, deepcopy
from math import gcd

def find_repeat(ci):
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
  # when does coord start repeating?
  steps = 9999999999999
  ens = set()
  for t in range(1,steps+1):
    for i in range(0,len(velarr)-1):
      for j in range(i+1,len(velarr)):
        x1 = posarr[i][ci]
        x2 = posarr[j][ci]
        
        a1 = x1 - x2
        a2 = a1 - .01
        try:
          change = math.floor(a1 / abs(a1)) * -1
        except:
          change = 0
        velarr[i][ci] = velarr[i][ci] + change
        velarr[j][ci] = velarr[j][ci] - change

    for i in range(0,len(posarr)):
      posarr[i][ci] = posarr[i][ci] + velarr[i][ci]  

    s = '{0}{1}{2}{3}{4}{5}{6}{7}'.format(posarr[0][ci],posarr[1][ci],posarr[2][ci],posarr[3][ci],velarr[0][ci],velarr[1][ci],velarr[2][ci],velarr[3][ci])
    if s in ens:
      return(t-1)
    else:
      ens.add(s)  

# MAIN
start_secs = time.time()
x_repeat = find_repeat(0)
y_repeat = find_repeat(1)
z_repeat = find_repeat(2)

#find LCM least common multiplier among the times that each planet starts repeating
a = [x_repeat,y_repeat,z_repeat]
lcm = a[0]
for i in a[1:]:
  lcm = lcm*i//gcd(lcm, i)
print()
print('t: ' + str(lcm))  #answer: 279751820342592
print()

end_secs = time.time()
print('elapsed time: ' + str(end_secs - start_secs) + ' seconds')
