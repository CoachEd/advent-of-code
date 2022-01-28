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

count = 0
arr = [ [] for i in range(len(l)) ]
for i in range(len(l)):
  arr1 = l[i].replace('\t',' ').split(' ')
  arr[i] = [ int(n) for n in arr1 ]
  arr[i].sort()
  x = arr[i][0]
  y = arr[i][-1]
  count += (y-x)

print(count)


  


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
