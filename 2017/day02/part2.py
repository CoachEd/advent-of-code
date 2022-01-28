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
nums = []
for i in range(len(l)):
  arr1 = l[i].replace('\t',' ').split(' ')
  arr[i] = [ int(n) for n in arr1 ]
  arr[i].sort()

  for j in range(0,len(arr[i])-1):
    for k in range(j+1,len(arr[i])):
      if arr[i][k] % arr[i][j] == 0:
        nums.append(arr[i][k]//arr[i][j])

for n in nums:
  count += n

print(count)


  


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
