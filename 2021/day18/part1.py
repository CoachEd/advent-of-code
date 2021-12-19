"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

start_secs = time.time()

def get_list(sn):
  if sn.isdigit():
    return int(sn)
  
  sn = sn[1:-1]
  comma_index = 0
  skips = 0
  for i in range(len(sn)):
    if sn[i] == '[':
      skips += 1
      continue
    
    if sn[i] == ',' and skips == 0:
      comma_index = i
      break
    
    if sn[i] == ',' and skips != 0:
      skips -= 1
      
  left = sn[0:comma_index]
  right = sn[comma_index+1:]
  return [ get_list(left) , get_list(right) ]

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

stree = []
for s in l:
  if len(stree) == 0:
    stree = get_list(s)
  else:
    stree = [ stree.copy() , get_list(s) ]

print(stree)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
