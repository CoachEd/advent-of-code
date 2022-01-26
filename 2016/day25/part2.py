"""
AoC
"""
import time
import sys
import math
from copy import copy, deepcopy

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

reg = {}
reg['a'] = 0
reg['b'] = 0
reg['c'] = 1
reg['d'] = 0

i = 0
while i < len(l):
  s = l[i]
  arr = s.split(' ')
  cmd = arr[0]
  arg1 = arr[1]
  arg2 = ''
  val = 0
  if len(arr) == 3:
    arg2 = arr[2]

  if cmd == 'cpy':
    if arg1.isalpha():
      val = reg[arg1]
    else:
      val = int(arg1)
    reg[arg2] = val
    i += 1
  elif cmd == 'inc':
    reg[arg1] += 1
    i += 1
  elif cmd == 'dec':
    reg[arg1] -= 1
    i += 1
  elif cmd == 'jnz':
    if arg1.isalpha():
      val = reg[arg1]
    else:
      val = int(arg1)
    if val != 0:
      i = i + int(arg2)
    else:
      i += 1

print(reg)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
