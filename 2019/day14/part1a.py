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

s = """157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT
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
  qty_requested = qty
  qty_avail = reaction[0]
  if qty >= qty_avail:
    divisor = qty // qty_avail 
    remainder = qty % qty_avail 
    if remainder > 0:
      divisor = divisor + 1
    qty = divisor  
  else:
    # got extra here
    qty = 1


  # TODO: leftovers
  # test case 3 has leftovers, but doesn't ever need to reuse them
  # test cases 1 & 2 do NOT have leftovers
  leftover = (qty * qty_avail) - qty_requested
  if leftover > 0:
    print('extra ' + name + ': ' + str(leftover))


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
