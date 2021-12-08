# part 1

"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

digits = [0,2,0,0,4,0,0,3,7]
count = 0
for s in l:
  arr = s.split('|')
  arr2 = arr[1].split()
  for o in arr2:
    n = len(o)
    if n in digits:
      count += 1

print(count)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
