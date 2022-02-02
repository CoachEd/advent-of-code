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

def process_op(reg,instr,amt,r):
  if instr == 'inc':
    r[reg] += amt
  elif instr == 'dec':
    r[reg] -= amt
  else:
    print('unknown instr: ' + instr)

def eval_op(op1,op2,operand,r):
  if operand == '>':
    return r[op1] > op2
  if operand == '<':
    return r[op1] < op2
  if operand == '>=':
    return r[op1] >= op2
  if operand == '<=':
    return r[op1] <= op2
  if operand == '==':
    return r[op1] == op2
  if operand == '!=':
    return r[op1] != op2
  print('ERROR: ' + operand)
              
start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

# add all registers
r = {}
max_val = -sys.maxsize - 1
for s in l:
  arr = s.split(' ')
  if arr[0] not in r:
    r[ arr[0] ] = 0
  
for s in l:
  arr = s.split(' ')
  reg = arr[0]
  instr = arr[1]
  amt = int(arr[2])
  op1 = arr[4]
  operand = arr[5]
  op2 = int(arr[6])
  if eval_op(op1,op2,operand,r):
    process_op(reg,instr,amt,r)
    for keu,val in r.items():
      if val > max_val:
        max_val = val

print(max_val)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
