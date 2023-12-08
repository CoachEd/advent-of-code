# Day 8 part 1
import time
import sys
from copy import copy, deepcopy
from itertools import cycle

start_secs = time.time()
print('')
 
# SOLUTION
# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

instr = [ c for c in l[0] ]
instr = cycle(instr)
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

node = 'AAA'
steps = 0
while True:
  if node == 'ZZZ':
    break
  c = next(instr)
  node = d[node][c]
  steps += 1
  
print(steps)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')