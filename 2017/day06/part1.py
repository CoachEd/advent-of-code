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

arr = [ int(n) for n in l[0].split('\t') ]

cycles = 0
d = set()
while True:
  # get biggest
  i = -1
  val = -1
  for j in range(len(arr)):
    if arr[j] > val:
      i = j
      val = arr[j]
  
  divisor = val // len(arr)
  remainder = val % len(arr)
  arr[i] = 0
  for j in range(len(arr)):
    arr[j] += divisor
  k = i+1
  if k >= len(arr):
    k = 0
  for j in range(remainder):
    arr[k] += 1
    k += 1
    if k >= len(arr):
      k = 0
  t = tuple(arr)
  # print(t) debug
  cycles += 1
  if t in d:
    break
  d.add(t)

print(cycles)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
