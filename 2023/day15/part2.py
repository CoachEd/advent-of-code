

# D15 Part 2

import time
import sys
from copy import copy, deepcopy 

# read in input file
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
l=[None for i in range(len(lines))]
for i in range(len(lines)):
  l[i] = lines[i].strip()

# SOLUTION START - start timing
start_secs = time.time()
d = {}
def decode(s):
  n = 0
  for c in s:
    x = ord(c)
    n += x
    n *= 17
    n %= 256
  return n

arr = l[0].split(',')
tot = 0
dvals = {} # 0rn , 1qp, ...
for s in arr:
  if '=' in s:
    # put
    cmd = s.split('=')
    label = cmd[0]
    box = decode(label)
    num = int(cmd[1])
    #print((box,label,num))
    if not box in d:
      d[box] = []
    if not label in d[box]:
      d[box].append(label)
    dvals[str(box)+label] = num
  else:
    # del
    cmd = s.split('-')
    label = cmd[0]
    box = decode(label)
    k = str(box)+label
    if k in dvals:
      del dvals[str(box)+label]
    if box in d:
      if label in d[box]:
        d[box].remove(label)

"""
for k,v in d.items():
  print((k,v))
  
print(dvals)
"""
tot = 0
for b in range(0,256):
  box = b
  if box in d:
    for label in d[box]:
      n = dvals[ str(box)+label]
      fp = (1+box) * (d[box].index(label)+1)*n
      tot += fp
print(tot)
    




end_secs = time.time()

print('--- ' + str(end_secs-start_secs) + ' secs ---')

# SOLUTION END - stop timing
