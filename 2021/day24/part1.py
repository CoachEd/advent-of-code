# part 1
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
my_file = open("inp2.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

d = {}
d['w']=0
d['x']=0
d['y']=0
d['z']=0

commands =[]
for s in l:
  arr = s.split()
  args =[]
  instr = arr[0]
  for i in range(1, len(arr)):
    if arr[i].isdigit() or arr[i].startswith('-'):
      args.append(int(arr[i]))
    else:
      args.append(arr[i])
  commands.append([instr]+args)

def execute_commands(inp):
  global d
  d['w']=0
  d['x']=0
  d['y']=0
  d['z']=0
  valid = True
  for c in commands:
    b = None
    if c[0] != 'inp':
      b = c[2]
      if isinstance(b, str):
        b = d[b]
    if c[0] == 'inp':
      d[c[1]]=inp.pop(0)
    elif c[0] == 'add':
      d[c[1]] = d[c[1]] + b
    elif c[0] == 'mul':
      d[c[1]] = d[c[1]] * b
    elif c[0] == 'div':
      if b == 0:
        valid = False
        break
      d[c[1]] = int(d[c[1]] / b)
    elif c[0] == 'mod':
      if b < 0:
        valid = False
        break
      d[c[1]] = d[c[1]] % b
    elif c[0] == 'eql':
      res = 0
      if d[c[1]] == b:
        res = 1
      d[c[1]] = res

  if valid and d['z'] == 0:
    return True
  else:
    return False
    
print( execute_commands([1,3]) )
print(d)
    
  


end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')