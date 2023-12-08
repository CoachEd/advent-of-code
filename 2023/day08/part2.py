# Day 8 part 2
import time
import sys
import math
import re
from copy import copy, deepcopy
from itertools import cycle
from functools import reduce

# USE math.lcm() <-- takes comma-separated args (convert arr this way: *arr)
# search terms: lcm LCM LCD lcd gcf gcd
# least common multiple of list
# i.e., when you want n repeating numbers to line up
# e.g., a = [3, 5, 15] , math.lcm(*a) => 15
# a repeats every 3, b repeats every 5, c repeats ever 15
# the first number where they all line up is 15
#
# 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
# ----------------------------------------------------
#          a        a        a       a        a
#                b             b              b
#                                             c       

start_secs = time.time()

# SOLUTION
# read in input file
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
l=[None for i in range(len(lines))]
for i in range(len(lines)):
  l[i] = re.sub(r'=|\(|\)|,', '', lines[i].strip())

instr1 = [ c for c in l[0] ]
del l[0]
del l[0]

d = {}
# AAA = (BBB, BBB)
for s in l:
  arr = s.split()
  k = arr[0]
  d[k] = {}
  d[k]['L'] = arr[1]
  d[k]['R'] = arr[2]

nodes = []
for k,v in d.items():
  if k.endswith('A'):
    nodes.append(k)

nums = [0 for i in range(len(nodes))]
instructions = cycle(instr1)
for i in range(len(nodes)):
  node = nodes[i]
  steps = 0
  while True:
    if node[-1] == 'Z':
      nums[i] = steps
      break
    c = next(instructions)
    node = d[node][c]
    steps += 1

print(math.lcm(*nums))
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')