# part 1


"""
AoC
"""
import time
import sys
from copy import copy, deepcopy
d = {}
counts = {}

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

s = l[0]
for i in range(2,len(l)):
  a = l[i].split(' -> ')
  d[ a[0] ] = a[1]

# get initial counts
for c in s:
  if not c in counts:
    counts[c] = 0
  counts[c] += 1

# add segs
dsegs = {}
for i in range(0, len(s)-1):
  seg = s[i:i+2]
  if not seg in dsegs:
    dsegs[seg] = 0
  dsegs[seg] += 1

for i in range(40):
  # loop through all segs, add counts, adjust segs
  print(str(i+1))
  dsegs1 = dsegs.copy()
  for seg in dsegs:
    if seg in d:
      n = dsegs[seg]
      for i in range(n):
        dsegs1[seg] -= 1
        if dsegs1[seg] == 0:
          del dsegs1[seg]
        insrt = d[seg]
        if not insrt in counts:
          counts[insrt] = 0
        counts[insrt] += 1
        seg1 = seg[0] + insrt
        seg2 = insrt + seg[1]
        if not seg1 in dsegs1:
          dsegs1[seg1] = 0
        if not seg2 in dsegs1:
          dsegs1[seg2] = 0
        dsegs1[seg1] += 1
        dsegs1[seg2] += 1
  dsegs = dsegs1.copy()          

mx = 0
mn = sys.maxsize
for key in counts:
  if counts[key] > mx:
    mx = counts[key]
  if counts[key] < mn:
    mn = counts[key]
print(str(mx-mn))

end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
