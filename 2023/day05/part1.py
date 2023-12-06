import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')


# SOLUTION

def getIndex(n,mapnum):
  global maps
  # given an number n and the map number (0-6)
  # search the ranges in that map number to conver it
  # if not found, just return the number itself
  # return the number that it maps to
  for t in maps[mapnum]:
    (s0,s1,d0,d1) = (t)
    if n >= s0 and n <= s1:
      # found the range
      n1 = n - s0 + d0
      return n1
  return n

# read in input file
l=[]
my_file = open("inp2.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

a = l[0].split()
del a[0]
seeds = [ int(x) for x in a]

del l[0]
del l[0]

maps = [ [] for i in range(7) ] # each element is an array of ranges (s0,s1,d0,d1)
i = 0
map_num = -1
while i < len(l):
  s = l[i].strip()
  if len(s) == 0:
    # end of data
    i += 1
    continue
  elif s.find(':') != -1:
    # header
    map_num += 1
    a = s.split()
    #print(a[0])
  else:
    # ranges
    a0 = l[i].split()
    src = int(a0[1])
    dest = int(a0[0])
    l1 = int(a0[2])
    s0 = src
    s1 = src + l1 - 1
    d0 = dest
    d1 = dest + l1 - 1 
    maps[map_num].append((s0,s1,d0,d1))
  i += 1

min_loc = sys.maxsize
for s in seeds:
  start_num = s
  for i in range(len(maps)):
    start_num = getIndex(start_num, i)
  if start_num < min_loc:
    min_loc = start_num
  

print()
print(min_loc)


# 2369219742 too high

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')