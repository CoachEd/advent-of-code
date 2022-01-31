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

d = {}
for s in l:
  arr = s.split(' -> ')
  arr2 = arr[0].split(' ')
  node = arr2[0]
  if not node in d:
    d[node] = [[],[]]  # [ [above] , [below] ]  
  if len(arr) > 1:
    # process above and below
    arr3 = arr[1].split(', ')
    # above
    for s2 in arr3:
      d[node][0].append(s2)
      if not s2 in d:
        d[s2] = [[],[]]  # [ [above] , [below] ]  
      d[s2][1].append(node)


for key,val in d.items():
  if len(val[1]) == 0:
    print(key)
    

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
