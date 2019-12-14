import sys
import time
import math
from copy import copy, deepcopy
import cProfile, pstats
from io import StringIO

"""
pr = cProfile.Profile()  # create a profile object
pr.enable()  # start profiling
"""

start_secs = time.time()

s = """2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF
"""

arr = s.split('\n')[:-1]
reactions = {}
primitives = []
for l in arr:
  arr2 = l.split("=>")
  
  # process left side
  reaction = arr2[0].strip()
  reaction = reaction.replace(',','')
  temparr1 = []
  arr3 = reaction.split(' ')
  found_primitive = False
  for c in arr3:
    if c == 'ORE':
      found_primitive = True
    if c.isnumeric():
      temparr1.append(int(c))
    else:
      temparr1.append(c)

  # process right side
  produces = arr2[1].strip()
  arr3 = produces.split(' ')
  key = arr3[1]
  qty = arr3[0]
  if found_primitive:
    primitives.append(key)
  temparr2 = []
  temparr2.append(int(qty))
  temparr2.append(key)
  temparr2.extend(temparr1)
  reactions[key] = temparr2

print('primitives: ' + str(primitives))
for k in reactions:
  print(k + ': ' + str(reactions[k]))




def countPrimitive(qty,name,primitive):
  reaction = reactions[name]

  if reaction[3] == 'ORE' and name == primitive:
    # found a primitive
    return qty
  
  if reaction[3] == 'ORE':
    return 0

  # NEW
  qty_avail = reaction[0]
  if qty >= qty_avail:
    divisor = qty // qty_avail 
    remainder = qty % qty_avail 
    if remainder > 0:
      divisor = divisor + 1
    qty = divisor  
  else:
    # got extra here
    #qty = qty_avail
    qty = 1

  total = 0
  for i in range(2,len(reaction),2):
    total = total + qty * countPrimitive(reaction[i],reaction[i+1],primitive)

  return total



# count needed ore
total_ore = 0
#primitives = ["VJHF"] # test
for name in primitives:
  needed_primitive = countPrimitive(1,"FUEL",name)
  #print('needed ' + name + ': ' + str(needed_primitive))
  r = reactions[name]
  qty_prim = r[0]
  #print('needed_primitive: ' + str(needed_primitive))
  qty_ore = r[2]
  total_primitive = 0
  while total_primitive < needed_primitive:
    total_primitive = total_primitive + qty_prim
    total_ore = total_ore + qty_ore

print(total_ore)



"""
pr.disable()  # end profiling

# print out some stats.
s = StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
"""

end_secs = time.time()
print('elapsed time: ' + str(end_secs - start_secs) + ' seconds')
