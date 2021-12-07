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

arr = l[0].split(',')
arr2 = arr.copy()
arr2.sort()
sm = int(arr2[0])
bg = int(arr2[-1])

minpos = -1
minfuel = sys.maxsize
for pos in range(sm, bg+1):
  fuel = 0
  for n in arr:
    fuel += abs(int(n) - pos)
  if fuel < minfuel:
    minfuel = fuel
    minpos = pos

print(minfuel)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
