import time
import sys
from ast import literal_eval
from copy import copy, deepcopy
start_secs = time.time()

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

  if isInt(left) and isInt(right):
    if left <= right:
      return True # correct order or continue comparing
    else:
      return False # wrong order

  if isList(left) and isList(right):
    if len(left) == 0 and len(right) == 0:
      return True
    if len(left) == 0 and len(right) > 0:
      return True
    if len(left) > 0 and len(right) == 0:
      return False
    l0 = left[0]
    r0 = right[0]
    if isOrder(l0,r0):
      return isOrder(left[1:],right[1:])
    else:
      return False

  # no need to worry about running out of items
  if isInt(left) and isList(right):
    return left < right[0]
  if isList(left) and isInt(right):
    return left[0] < right

# main
index = 1
tot = 0
for i in range(0, len(l), +3):
  left = literal_eval(l[i])
  right = literal_eval(l[i+1])
  if isOrder(left, right):
    tot += index
  index += 1

print(tot)

end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')