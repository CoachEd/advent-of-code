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

s = l[0]

arr2 = []
i=len(s)//2
for j in range(len(s)):
  arr2.append(i)
  i += 1
  if i == len(s):
    i = 0

i = 0
tot = 0
nums = []
while i < len(s):
  num = -1
  if s[i] == s[arr2[i]]:
    num = int(s[i])
  if num != -1:
    nums.append(num)
  i += 1

for n in nums:
  tot += n
print(tot)

# 1192 - WRONG too low

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
