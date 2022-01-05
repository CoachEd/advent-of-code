"""
AoC
"""
import time
import random
from random import randrange

mindex = {}
f = {}
E = 1 # current floor

""" real data
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
"""

""" test data """
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
      print('nm1: ' + nm1)
      print('nm2: ' + nm2)
      print('direction: ' + direction)
      print(str(arr))
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

  arr = f[E]  # current floor

  # move params
  m1 = ''
  m2 = ''
  direction = ''

  arr_unmatched = get_unmatched(arr)

  # algorithm

  if E < 4:
    # move up rules

    # if you have a match on the current floor, just move it to the top - safe
    (m1,m2) = get_matched(arr)
    if len(m1) > 0:
      return (m1,m2,'up')
    
    # if one on this floor has a match above, move that single one up
    for h in arr_unmatched:
      h2 = get_match(h)
      if h2 in f[E+1]:
        return (h,'','up')

  if E > 1:
    # move down rules
    
    # who can safely move down
    arr_unmatched_below = get_unmatched(f[E-1])
    candidates = get_items_only(arr)
    if len(arr_unmatched_below) > 0:
      # all unmatched have to be the same device type
      c = arr_unmatched_below[0][1]
      


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
for i in range(20):
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
