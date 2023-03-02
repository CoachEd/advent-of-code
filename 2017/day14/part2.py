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

def valid(y,x):
  global rows, cols
  if y < 0 or x < 0 or y >= rows or x >= cols:
    return False
  return True

def find_region(d, y, x, region_number):
  if valid(y,x) and d[y][x] == '#':
    d[y][x] = region_number
  (ty,tx,by,bx,ry,rx,ly,lx) = (y-1,x,y+1,x,y,x+1,y,x-1)
  if valid(ty,tx) and d[ty][tx] == '#':
    find_region(d,ty,tx,region_number)
  if valid(by,bx) and d[by][bx] == '#':    
    find_region(d,by,bx,region_number)
  if valid(ry,rx) and d[ry][rx] == '#':
    find_region(d,ry,rx,region_number)
  if valid(ly,lx) and d[ly][lx] == '#':  
    find_region(d,ly,lx,region_number)

def find_regions(d, rows, cols):
  global region_number
  for y in range(rows):
    for x in range(cols):
      if d[y][x] == '#':
        # used square
        region_number += 1
        find_region(d, y, x, region_number)
      else:
        # skip
        continue

def print_disk(d):
  s = ''
  for y in range(8):
    for x in range(8):
      s += str(d[y][x])
    s += '\n'
  print(s)


def knot_hash(key_str):
  l1 = []
  l2 = [17, 31, 73, 47, 23]
  for c in key_str:
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

  s4 = ''
  for c in s:
    s4 += bin(int(c,16))[2:].zfill(4)
    if len(s4) == 128:
      break
  return s4

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

key_str = 'jzgqcdpd'
#key_str = 'flqrgnkx'  # sample test
disk = []
for i in range(128):
  s = knot_hash(key_str + '-' + str(i))
  s = s.replace('1', '#')
  s = s.replace('0', '.')
  tarr = [ c for c in s ]
  disk.append(tarr)

region_number = 0
rows = len(disk)
cols = len(disk[0])

find_regions(disk, rows, cols)

print(region_number)

# 30 wrong
# 27 wrong

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
