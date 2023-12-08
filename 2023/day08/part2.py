# Day 8 part 2
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
steps = 0
instructions = [ cycle(instr1) for i in range(len(nodes)) ]
while True:
  
  done = True
  for n in nodes:
    if not n.endswith('Z'):
      done = False
      break
  if done:
    break
    
  for i in range(len(nodes)):
    c = next(instructions[i])
    src = nodes[i]
    nodes[i] =  d[nodes[i]][c]
    #print((src,c,nodes[i]))
  steps += 1

print(steps)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')