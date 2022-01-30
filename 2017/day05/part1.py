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

arr = [ int(n) for n in l ]
pos = 0
steps = 0
while pos >= 0 and pos < len(arr):
  steps += 1
  curr_num = arr[pos]
  arr[pos] += 1
  pos += curr_num
  
print(steps)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
