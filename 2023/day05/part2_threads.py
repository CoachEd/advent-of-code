import time
import sys
import threading
from copy import copy, deepcopy
start_secs = time.time()
print('')


# SOLUTION
# WOW - TOOK --- 24624.036353111267 secs ---
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

def processRange(r,t):
  print('processing range...')
  min_loc = sys.maxsize
  (s,e) = t
  for s in range(s,e+1):
    start_num = s
    for i in range(len(maps)):
      start_num = getIndex(start_num, i)
    if start_num < min_loc:
      min_loc = start_num
  print('Range ' + str(r) + ':    min_loc: ' + str(min_loc))  
  
# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

"""
print('creating seeds...')
seed_start = 3995609239
seed_end =   4138877354
len1 = seed_end - seed_start + 1
seeds = [ None for i in range(len1) ]
index = 0
for i in range(seed_start, seed_end+1):
  seeds[index] = i
  index += 1
  
# seed_end - seed_start = 143268115
"""
a = l[0].split()
del a[0]
a1 = [ int(x) for x in a ]
seed_ranges = []
for i in range(0,len(a1),2):
  start = int(a1[i])
  end = start + int(a1[i+1])-1
  seed_ranges.append((start,end))

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

"""
#print('reduce maps...')

#n = reduceMap(35,6)
n = reduceMap(551761867,6)

n = reduceMap(n, 5)
n = reduceMap(n, 4)
n = reduceMap(n, 3)
n = reduceMap(n, 2)
n = reduceMap(n, 1)
n = reduceMap(n, 0)
"""

print()
"""
range_num = 0
i = 0
for t in seed_ranges:
 
 processRange(i,t)
 i += 1
"""
t1 = threading.Thread(target=processRange, args=(0,seed_ranges[0],))
t2 = threading.Thread(target=processRange, args=(1,seed_ranges[1],))
t3 = threading.Thread(target=processRange, args=(2,seed_ranges[2],))
t4 = threading.Thread(target=processRange, args=(3,seed_ranges[3],))
t5 = threading.Thread(target=processRange, args=(4,seed_ranges[4],))
t6 = threading.Thread(target=processRange, args=(5,seed_ranges[5],))
t7 = threading.Thread(target=processRange, args=(6,seed_ranges[6],))
t8 = threading.Thread(target=processRange, args=(7,seed_ranges[7],))
t9 = threading.Thread(target=processRange, args=(8,seed_ranges[8],))
t10 = threading.Thread(target=processRange, args=(9,seed_ranges[9],))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()

#print()
#print(min_loc)

# 15998365 too low

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')