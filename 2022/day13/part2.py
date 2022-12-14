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
  l2 = line.strip()
  if len(l2) > 0:
    l.append( literal_eval(line.strip()))
l.append( literal_eval('[[2]]'))
l.append( literal_eval('[[6]]'))

def isInt(x):
  return isinstance(x, int)

def isList(x):
  return type(x) is list

def isOrder(left,right):
  # two lists as input parameters

  # if both are integers
  if isInt(left) and isInt(right):  
    if left < right:
      return True
    elif left > right:
      return False
    else:
      return 2

  # if one is a list and one is an integer, make the integer a list
  if isList(left) and isInt(right):
    right = [right]
  elif isInt(left) and isList(right):
    left = [left]

  # we now have TWO lists

  # run out of items?
  if len(left) == 0 and len(right) > 0:
    return True
  if len(left) > 0 and len(right) == 0:
    return False

  # loop through first elements and compare them

  # special case for empty lists. NEEDED?
  if len(left) == 0 and len(right) == 0:
    left = [0]
    right = [0]

  rval = 2
  for i in range(len(left)):
    if (i >= len(right)):
      # right ran out
      return False
    rval = isOrder(left[i], right[i])
    if rval != 2:
      return rval

  # run out of items?
  if len(left) < len(right):
    return True

  return rval

def selectionSort(array, size):
  for ind in range(size):
      min_index = ind
      for j in range(ind + 1, size):
          if isOrder(array[j], array[min_index]):
              min_index = j
      (array[ind], array[min_index]) = (array[min_index], array[ind])

# main
index = 1
tot = 0

selectionSort(l, len(l))
p1 = -1
p2 = -1
for i in range(len(l)):
  if str(l[i]) == '[[2]]':
    p1 = i + 1
  if str(l[i]) == '[[6]]':
    p2 = i + 1

print(p1 * p2)

end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')