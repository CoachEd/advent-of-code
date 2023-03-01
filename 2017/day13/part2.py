import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')


# SOLUTION

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

sz = dict()
last_snum = None
for s in l:
  s = s.split(': ')
  snum = int(s[0])
  slen = int(s[1])
  sz[snum] = slen
  last_snum = snum

#factor = len - 2 * 2 + 2
# delay + snum cannot be that col's factor

factors = dict()
for e in sz:
  factor = (sz[e] - 2) * 2 + 2
  factors[e] = factor
  #print(str(e) + ' , ' + str(sz[e]) + ' , ' + str(factor))

max_delay = 10000000
for d in range(max_delay):
  found = True
  for e in sz:
    x = d + e
    f = factors[e]
    if x % f == 0:
      found = False
      break
  if found:
    print(d)
    break


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')