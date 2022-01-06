"""
AoC
"""
import time
import random
from random import randrange

mindex = {}
f = {}
E = 1 # current floor


mindex['MG'] = 0
mindex['MM'] = 1
mindex['RG'] = 2
mindex['RM'] = 3
mindex['PM'] = 4
mindex['PG'] = 5
mindex['SM'] = 6
mindex['SG'] = 7
mindex['TG'] = 8
mindex['TM'] = 9

f[4] = ['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ']
f[3] = ['MG','MM','RG','RM','  ','  ','  ','  ','  ','  ']
f[2] = ['  ','  ','  ','  ','PM','  ','SM','  ','  ','  ']
f[1] = ['  ','  ','  ','  ','  ','PG','  ','SG','TG','TM']


""" test data
# start test data
mindex['HG'] = 0
mindex['HM'] = 1
mindex['LG'] = 2
mindex['LM'] = 3

f[4] = ['  ','  ','  ','  ']
f[3] = ['  ','  ','LG','  ']
f[2] = ['HG','  ','  ','  ']
f[1] = ['  ','HM','  ','LM']
# end test data
"""

def get_match(s):
  c1 = s[0]
  c2 = s[1]
  c3 = 'G'
  if c2 == 'G':
    c3 = 'M'
  return(c1 + c3)

def move_item(nm1, nm2, direction):
  global E
  global f
  global mindex
  if direction == 'down' and E > 1:
    if nm1 != '':
      arr = f[E]
      if arr[ mindex[nm1] ] == nm1:
        arr[ mindex[nm1] ] = '  '
        arr = f[E-1]
        arr[ mindex[nm1] ] = nm1
    if nm2 != '':
      arr = f[E]
      if arr[ mindex[nm2] ] == nm2:
        arr[ mindex[nm2] ] = '  '
        arr = f[E-1]
        arr[ mindex[nm2] ] = nm2    
    E -= 1
  elif direction =='up' and E < 4:
    if nm1 != '':
      arr = f[E]
      if arr[ mindex[nm1] ] == nm1:
        arr[ mindex[nm1] ] = '  '
        arr = f[E+1]
        arr[ mindex[nm1] ] = nm1
    if nm2 != '':
      arr = f[E]
      if arr[ mindex[nm2] ] == nm2:      
        arr[ mindex[nm2] ] = '  '
        arr = f[E+1]
        arr[ mindex[nm2] ] = nm2    
    E += 1

def match_on_floor(s,arr):
  # is s's match on the floor?
  c1 = s[0]
  c2 = s[1]
  c3 = 'G'
  if c2 == 'G':
    c3 = 'M'
  s2 = c1 + c3
  if s2 in arr:
    return s2
  return ''

def get_random(arr):
  i = randrange(len(arr))
  return arr[i]

def get_items_only(arr):
  arr2 = arr.copy()
  try:
    while True:
      arr2.remove('  ')
  except ValueError:
    pass
  return arr2

def get_unmatched_items_type(arr,t):
  arr = get_unmatched(arr).copy()
  arr2 = []
  for s in arr:
    if s[1] == t:
      arr2.append(s)
  return arr2

def get_matched(arr):
  # return a matching pair if found
  for h in arr:
    if h == '  ':
      continue
    h2 = match_on_floor(h,arr)
    if len(h2) > 0:
      return (h,h2)
  return ('','')

def is_safe(s,arr):
  # is it safe to but s on floor?
  c1 = s[1]
  c2 = 'G'
  if c1 == 'G':
    c2 = 'M'
  arr2 = get_unmatched_items_type(arr,c2)
  if len(arr2) > 0:
    return False
  return True

def count_items(arr):
  count = 0
  for s in arr:
    if s == '  ':
      continue
    count += 1
  return count

def get_unmatched(arr):
  # which ones are unmatched on the floor
  arr2 = []
  for s in arr:
    if s == '  ':
      continue
    s2 = match_on_floor(s,arr)
    if len(s2) == 0:
      arr2.append(s)
  return(arr2)

def floor_empty(arr):
  if len( (''.join(arr)).strip() ) == 0:
    return True
  return False

def get_move():
  global E
  global f
  global mindex

  if E == 1:
    # first floor
    
    # Rule: if we have a match on this floor, move them up
    (h1,h2) = get_matched(f[E])
    if h1 != '':
      return (h1,h2,'up')
    
    # Rule: if an unmatched item has a match above, move that one up
    unmatched = get_unmatched(f[E])
    unmatched_above = get_unmatched(f[E+1])
    for h1 in unmatched:
      h2 = get_match(h1)
      if h2 in unmatched_above:
        return (h1,h2,'up')

    # Rule: if we have two like, unmatched items, move them up if safe to    
    unmatched_ms = get_unmatched_items_type(f[E],'M')
    for i in range(len(unmatched_ms)-1):
      for j in range(i+1,len(unmatched_ms)):
        if is_safe(unmatched_ms[i],f[E+1]) and is_safe(unmatched_ms[j],f[E+1]):
          return (unmatched_ms[i],unmatched_ms[j],'up')
    unmatched_gs = get_unmatched_items_type(f[E],'G')
    for i in range(len(unmatched_gs)-1):
      for j in range(i+1,len(unmatched_gs)):
        if is_safe(unmatched_gs[i],f[E+1]) and is_safe(unmatched_gs[j],f[E+1]):
          return (unmatched_gs[i],unmatched_gs[j],'up')

  elif E == 4:
    # fourth floor
    
    # rule: if an unmatched has a match below
    unmatched = get_unmatched(f[E])
    unmatched_below = get_unmatched(f[E-1])
    for h in unmatched:
      h2 = get_match(h)
      if h2 in unmatched_below:
        return (h,'','down')

    # rule: pick one that's safe to move down
    unmatched_below = get_unmatched(f[E-1])
    for h in f[E]:
      if h == '  ':
        continue
      if is_safe(h,unmatched_below):
        return (h,'','down')

  elif E == 3:
    # third floor

    # rule: can I send an unmatched one down to get its match below?
    unmatched = get_unmatched(f[E])
    unmatched_floor2 = get_unmatched(f[E-1])
    unmatched_floor1 = get_unmatched(f[E-2])
    for h in unmatched:
      h2 = get_match(h)
      if h2 in unmatched_floor1 or h2 in unmatched_floor2:
        return (h,'','down')

    # Rule: if we have a match on this floor, move them up
    (h1,h2) = get_matched(f[E])
    if h1 != '':
      return (h1,h2,'up')
    
    # rule: if alone on floor and some below, move down
    if len(unmatched) == 1 and (count_items(f[E-1]) > 0 or count_items(f[E-2]) > 0):
      return (unmatched[0],'','down')

    # Rule: if an unmatched item has a match above, move that one up
    unmatched = get_unmatched(f[E])
    unmatched_above = get_unmatched(f[E+1])
    for h1 in unmatched:
      h2 = get_match(h1)
      if h2 in unmatched_above:
        return (h1,h2,'up')

    # Rule: if we have two like, unmatched items, move them up if safe to    
    unmatched_ms = get_unmatched_items_type(f[E],'M')
    for i in range(len(unmatched_ms)-1):
      for j in range(i+1,len(unmatched_ms)):
        if is_safe(unmatched_ms[i],f[E+1]) and is_safe(unmatched_ms[j],f[E+1]):
          return (unmatched_ms[i],unmatched_ms[j],'up')
    unmatched_gs = get_unmatched_items_type(f[E],'G')
    for i in range(len(unmatched_gs)-1):
      for j in range(i+1,len(unmatched_gs)):
        if is_safe(unmatched_gs[i],f[E+1]) and is_safe(unmatched_gs[j],f[E+1]):
          return (unmatched_gs[i],unmatched_gs[j],'up')    

  elif E == 2:
    # second floor
    # rule: can I send an unmatched one down to get its match below?
    unmatched = get_unmatched(f[E])
    unmatched_floor1 = get_unmatched(f[E-1])
    for h in unmatched:
      h2 = get_match(h)
      if h2 in unmatched_floor1:
        return (h,'','down')

    # rule: try to move up TODO
    # Rule: if we have a match on this floor, move them up
    (h1,h2) = get_matched(f[E])
    if h1 != '':
      return (h1,h2,'up')
    
    # rule: if alone on floor and some below, move down
    if len(unmatched) == 1 and count_items(f[E-1]) > 0:
      return (unmatched[0],'','down')

    # Rule: if an unmatched item has a match above, move that one up
    unmatched = get_unmatched(f[E])
    unmatched_above = get_unmatched(f[E+1])
    for h1 in unmatched:
      h2 = get_match(h1)
      if h2 in unmatched_above:
        return (h1,h2,'up')

    # Rule: if we have two like, unmatched items, move them up if safe to    
    unmatched_ms = get_unmatched_items_type(f[E],'M')
    for i in range(len(unmatched_ms)-1):
      for j in range(i+1,len(unmatched_ms)):
        if is_safe(unmatched_ms[i],f[E+1]) and is_safe(unmatched_ms[j],f[E+1]):
          return (unmatched_ms[i],unmatched_ms[j],'up')
    unmatched_gs = get_unmatched_items_type(f[E],'G')
    for i in range(len(unmatched_gs)-1):
      for j in range(i+1,len(unmatched_gs)):
        if is_safe(unmatched_gs[i],f[E+1]) and is_safe(unmatched_gs[j],f[E+1]):
          return (unmatched_gs[i],unmatched_gs[j],'up')



  # no rule!
  print('ERROR: No rule')
  return ('','','')

start_secs = time.time()

def print_floors():
  global E
  global f  
  s = ''
  for i in range(4,0,-1):
    arr = f[i]
    stemp = ''
    for j in range(len(arr)):
      stemp += arr[j] + ' '
    if i == E:
      stemp = ' E  ' + stemp
    else:
      stemp = '    ' + stemp
    stemp = 'F' + str(i) + stemp + '\n'
    s += stemp
  print(s)

print('')
print_floors()
steps = 0
for i in range(1000000):
  (nm1,nm2,direction) = get_move()
  if direction != '':
    move_item(nm1, nm2, direction)
    steps += 1
    print_floors()
 
  if not '  ' in f[4]:
    # done
    print('done')
    break

print(steps)



print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
