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

def reverse(arr,curr,len1):
  if len1 > len(arr):
    return
  sz = len(arr)
  endpos = ((len1+curr) % sz) - 1
  if endpos >= sz:
    endpos -= len1
  if endpos < 0:
    endpos = sz - 1

  for i in range( len1 // 2 ):
    temp = arr[curr]
    arr[curr] = arr[endpos]
    arr[endpos] = temp
    curr += 1
    if curr >= sz:
      curr = 0
    endpos -= 1
    if endpos < 0:
      endpos = sz - 1

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

l = [ int(n) for n in l[0].split(',') ]

LIST_SIZE = 256
arr = [ n for n in range(LIST_SIZE)]
curr = 0
skip = 0
sz = len(arr)
for len1 in l:
  #print('skip = ' + str(skip) + '  ' + '  curr = ' + str(curr) + '  len = ' + str(len1))
  #print(arr)
  reverse(arr,curr,len1)
  curr = (curr + len1 + skip) % sz
  skip += 1
  #print(arr)
  #print()

print(arr[0] * arr[1])

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
