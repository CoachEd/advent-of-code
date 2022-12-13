import time
import sys
from ast import literal_eval
from copy import copy, deepcopy
start_secs = time.time()
print()

# SOLUTION
# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

def isInt(x):
  return isinstance(x, int)

def isList(x):
  return type(x) is list

def isOrder(left,right):
  # two lists as input parameters

  for i in range(len(left)):
    if i >= len(right):
      return False  # right ran out
    l = left[i]
    r = right[i]
    # l and r are integers
    if isInt(l) and isInt(r):  
      if l < r:
        return True
      elif l > r:
        return False
    elif isList(l) and isList(r):
      # TODO: l and r are both lists
      pass
    elif isList(l) and isInt(r):
      # TODO: l is a list and r is an integer
      pass
    elif isInt(l) and isList(r):
      # TODO: l is an integer and r is a list
      pass



    
# main
index = 1
tot = 0
for i in range(0, len(l), +3):
  left = literal_eval(l[i])
  right = literal_eval(l[i+1])
  if isOrder(left, right):
    print('IN ORDER')
    tot += index
  else:
    print('NOT IN ORDER')
  index += 1

print()
print(tot)
# 358 TOO LOW

end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')