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

s = """9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL
"""

arr = s.split('\n')[:-1]
reactions = {}
surplus_dict = {}
elems_dict = {}
for l in arr:
  arr2 = l.split("=>")
  
  # process left side
  reaction = arr2[0].strip()
  reaction = reaction.replace(',','')
  temparr1 = []
  arr3 = reaction.split(' ')
  found_primitive = False
  for c in arr3:
    if c.isnumeric():
      temparr1.append(int(c))
    else:
      temparr1.append(c)

  # process right side
  produces = arr2[1].strip()
  arr3 = produces.split(' ')
  key = arr3[1]
  qty = arr3[0]
  temparr2 = []
  temparr2.append(int(qty))
  temparr2.append(key)
  temparr2.extend(temparr1)
  reactions[key] = temparr2


for k in reactions:
  print(k + ': ' + str(reactions[k]))

def countOre(qty_requested,elem):
  global reactions
  print('countOre ' + str(qty_requested) + ',' + elem)
  reaction = reactions[elem]
  qty_batch = reaction[0]

  if reaction[3] == 'ORE':
    if not elem in elems_dict:
      elems_dict[elem] = 0
    elems_dict[elem] = elems_dict[elem] + qty_requested
    return

  div = 1
  if qty_requested > qty_batch:
    div = qty_requested // qty_batch
    rem = qty_requested % qty_batch
    if rem > 0:
      div = div + 1

  """
  # try to use any surplus
  if not elem in surplus_dict:
    surplus_dict[elem] = 0
  surplus = surplus_dict[elem]
  if qty_requested <= surplus:
    surplus_dict[elem] = surplus - qty_requested
    return 0
  else:
    qty_requested = qty_requested - surplus
    surplus_dict[elem] = 0
  """

  """
  qty_needed = 1
  if qty_requested <= qty_batch:
    # request one batch; there may be surplus
    surplus_dict[elem] = surplus_dict[elem] + (qty_batch - qty_requested)
  else:
    # need multiple batches
    div = qty_requested // qty_batch
    rem = qty_requested % qty_batch
    qty_needed = div
    if rem > 0:
      qty_needed = qty_needed + 1
  """
  for i in range(2,len(reaction),2):
    countOre(div*reaction[i],reaction[i+1])

  return

print( countOre(1,'FUEL') )
print(elems_dict)

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
