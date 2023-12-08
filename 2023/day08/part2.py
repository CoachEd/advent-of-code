# Day 8 part 2
import time
import sys
import math
from copy import copy, deepcopy
from itertools import cycle
from functools import reduce

def lcm(a):
  # search terms: lcm LCM LCD lcd gcf gcd
  # least common multiple of list
  # i.e., when you want n repeating numbers to line up
  # e.g., a = [3, 5, 15] , lcm(a) => 15
  # a repeats every 3, b repeats every 5, c repeats ever 15
  # the first number where they all line up is 15
  #
  # 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
  # ----------------------------------------------------
  #          a        a        a       a        a
  #                b             b              b
  #                                             c       

  lcm = 1
  for i in a:
    lcm = lcm*i//math.gcd(lcm, i)
  return lcm

start_secs = time.time()
print('')

# SOLUTION
# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

instr1 = [ c for c in l[0] ]
del l[0]
del l[0]

d = {}
# AAA = (BBB, BBB)
for s in l:
  arr = s.split('=')
  k = arr[0].strip()
  arrb = arr[1].replace('(','').replace(')','').replace(',','').split()
  d[k] = {}
  d[k]['L'] = arrb[0]
  d[k]['R'] = arrb[1]

nodes = []
for k,v in d.items():
  if k.endswith('A'):
    nodes.append(k)

nums = []
for i in range(len(nodes)):
  node = nodes[i]
  steps = 0
  instructions = cycle(instr1)
  while True:
    if node.endswith('Z'):
      nums.append(steps)
      break
    c = next(instructions)
    node = d[node][c]
    steps += 1
    
print(lcm(nums))

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')