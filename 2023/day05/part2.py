import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')


# SOLUTION

def reduceMap6(min_loc):
  # given some min_loc, reduce the maps from the bottom up
  global maps
  start = 0
  end = min_loc
  i = len(maps)-1
  m = maps[i]
  m2 = m.copy()
  for t in m2:
    pass
  # keep ALL ranges (tuples) that have destination ranges including or less than min_loc

def reduceMapN(N):
  global maps
  map = maps[N]
  map_below = maps[N+1]
  # only keep tuples in map that have destinations that map to sources in map_below
  pass

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
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

print('creating seeds...')
seeds = []
a = l[0].split()
del a[0]
seeds = [ int(x) for x in a]

del l[0]
del l[0]

print('creating maps...')
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


print('reduce maps...')
#reduceMap6(46)
reduceMap6(551761867) # this should still result in the answer 551761867, but it doesn't. why?

print()

min_loc = sys.maxsize
for s in seeds:
  start_num = s
  for i in range(len(maps)):
    start_num = getIndex(start_num, i)
  if start_num < min_loc:
    min_loc = start_num
  #print(str(s) + ' --> ' + str(start_num))
  
print()
print(min_loc)

# 22652094 too low

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')