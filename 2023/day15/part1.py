# D15 Part 1
import time
import sys
from copy import copy, deepcopy 

# read in input file
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
l=[None for i in range(len(lines))]
for i in range(len(lines)):
  l[i] = lines[i].strip()

# SOLUTION START - start timing
start_secs = time.time()

def decode(s):
  n = 0
  for c in s:
    x = ord(c)
    n += x
    n *= 17
    n %= 256
  return n

arr = l[0].split(',')
tot = 0
for s in arr:
  tot += decode(s)
print(tot)



end_secs = time.time()

print('--- ' + str(end_secs-start_secs) + ' secs ---')

# SOLUTION END - stop timing

