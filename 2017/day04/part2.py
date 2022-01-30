"""
AoC
"""
import time
import sys
import random
import math
from random import randrange
from copy import copy, deepcopy
from itertools import permutations

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

valid = 0
sorted_arr = [ '' for i in range(len(l)) ]
for x in range(len(l)):
  p = l[x]
  arr = p.split(' ')
  for i in range(len(arr)):
    arr2 = [ c for c in arr[i] ]
    arr2.sort()
    arr[i] = ''.join(arr2)
  unique = set()
  for t in arr:
    unique.add(t)
  if len(arr) == len(unique):
    valid += 1

print(valid)


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
