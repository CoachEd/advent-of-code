import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')


# SOLUTION

def reduceMap(n,i):
  # n is max dest vale we care about
  # i is the map we are reducing
  global maps
  start = 0
  m = maps[i]
  m2 = []
  max_s1 = -1
  for t in m:
    (s0,s1,d0,d1) = t
    # if range is beyond n, throw it out, otherwise, keep it
    if d0 > n:
      pass
    else:
      m2.append(t)
      if s1 > max_s1:
        max_s1 = s1
  m.clear()
  m += m2
  if len(m2) == 0:
    # no ranges contain n
    return n
  else:
    return max_s1


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

#print(maps[5])
print('reduce maps...')
n = reduceMap(35,6)
n = reduceMap(n, 5)
n = reduceMap(n, 4)
n = reduceMap(n, 3)
n = reduceMap(n, 2)
n = reduceMap(n, 1)
n = reduceMap(n, 0)



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