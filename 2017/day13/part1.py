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

sev = 0
for snum in range(last_snum+1):
  
  if not snum in d:
    move_scanners(d, direction, pos, sz)
    continue

  if pos[snum] == 0:
    sev += snum * sz[snum]
  move_scanners(d, direction, pos, sz)

print(sev)


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')