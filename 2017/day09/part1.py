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

# negate chars
arr = [ c for c in l[0] ]
for i in range(len(arr)):
  if arr[i] == '!' and i < len(arr)-1:
    arr[i+1] = ''
s = ''.join(arr)
print(s)

# remove garbage
arr = [ c for c in s ]
while True:
  if '<' in arr and '>' in arr:
    less_than = arr.index('<')
    greater_than = arr.index('>')
    for i in range(less_than,greater_than+1):
      arr[i] = ''
  else:
    break
s = ''.join(arr)
print(s)


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
