import time
import sys
from copy import copy, deepcopy
from itertools import cycle, islice, tee
start_secs = time.time()
print('')

def get_sequence(start_i, n, direction):
  arr = []
  for k in range(0, n):
    arr.append(k)
  for j in range(n-2, 0, -1):
    arr.append(j)
  pool = cycle(arr)
  arr = []
  for i in range(100):
    arr.append(next(pool))

  first_occurence = arr.index(start_i)
  second_occurrence = arr.index(start_i, first_occurence + 1)
  if direction == 'd':
    return arr[first_occurence:]
  else:
    return arr[second_occurrence:]

#arr = get_sequence(6, 7, 'u')

# SOLUTION
def nth(iterable, n, default=None):
  return next(islice(iterable, n, None), default)

def create_pool(n):
  arr = []
  for k in range(0, n):
    arr.append(k)
  for j in range(n-2, 0, -1):
    arr.append(j)
  pool = cycle(arr)
  return pool

"""
p = create_pool(5)
p, p1 = tee(p)
print( nth(p1, 0) )

p, p1 = tee(p)
print( nth(p1, 1) )
"""

pools = dict()

def move_scanners(d1, direction1, pos1, sz1):
  for snum in d1:
    pos = pos1[snum]
    direction = direction1[snum]
    new_pos = None
    new_dir = None
    sz = sz1[snum]
    if direction == 'd':
      new_dir = 'd'
      new_pos = pos + 1
      if new_pos >= sz:
        new_pos = pos - 1
        new_dir = 'u'
    else:
      new_dir = 'u'      
      new_pos = pos - 1
      if new_pos < 0:
        new_pos = pos + 1
        new_dir = 'd'
    d1[snum][pos] = ' '
    d1[snum][new_pos] = 'S'
    direction1[snum] = new_dir
    pos1[snum] = new_pos

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

d = dict()
direction = dict()
pos = dict()
sz = dict()
last_snum = None
for s in l:
  s = s.split(': ')
  snum = int(s[0])
  slen = int(s[1])
  d[snum] = [' '] * slen
  direction[snum] = 'd'  # or 'u'
  pos[snum] = 0
  sz[snum] = slen
  last_snum = snum

for e in d:
  d[e][0] = 'S'

#print(d) # initial
d_orig = deepcopy(d)
pos_orig = deepcopy(pos)
direction_orig = deepcopy(direction)

delay = 1000000
for i in range(1, delay + 1):
  # init dicts
  if i % 100 == 0:
    print(i)
  d = deepcopy(d_orig)
  pos= deepcopy(pos_orig)
  direction = deepcopy(direction_orig)

  for x in range(i): 
    move_scanners(d, direction, pos, sz)
  
  found = True
  for snum in d:
    pos1 = pos[snum]
    dir1 = direction[snum]
    sz1 = sz[snum]
    key = str(pos1) + ':' + str(sz1) + ':' + dir1
    if not key in pools:
      pools[key] = get_sequence(pos1, sz1, dir1)
    pool = pools[key]

    if snum == 0:
      if pos1 == 0:
        found = False
        break
      else:
        continue

    future_pos = pool[snum]
    if future_pos == 0:
      found = False
      break

  if found:
    print()
    print(i)
    break
  else:
    #print('not found')
    pass


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')