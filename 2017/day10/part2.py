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

l1 = []
l2 = [17, 31, 73, 47, 23]
for c in l[0]:
  l1.append(ord(c))
l = l1 + l2
l0 = l.copy()

LIST_SIZE = 256
arr = [ n for n in range(LIST_SIZE)]

curr = 0
skip = 0
for i in range(64):
  sz = len(arr)
  for len1 in l:
    reverse(arr,curr,len1)
    curr = (curr + len1 + skip) % sz
    skip += 1

l3 = []
for i in range(0, 256, 16):
  n = arr[i]
  for j in range(i+1, i+16, 1):
    n = n ^ arr[j]
  l3.append(n)

s = ''
for n in l3:
  hx = "0x{:02x}".format(n)
  s += hx[2:]

print(s)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
