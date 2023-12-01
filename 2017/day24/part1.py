import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')


# SOLUTION
# read in input file
components=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  components.append(line.strip())

def getEnds(s):
  a = s.split('/')
  return (int(a[0]), int(a[1]))

def canConnect(c,n):
  # can component c connect to value n?
  # if so, return other side
  # if not, return -1
  (x,y) = getEnds(c)
  if x == n:
    return y
  elif y == n:
    return x
  else:
    return -1

def getStartingPoints(n,l):
  # n is the value
  # l is the component list
  # return dictionary with c : l2  entries where
  # c is the starting node and l2 is the remaining list
  d = {} # component : list
  for c in l:
    (x,y) = getEnds(c)
    if x == n or y == n:
      arr1 = l.copy()
      arr1.remove(c)
      d[c] = arr1
  return d

def getBridges(c, n, l):
  # TODO
  # get the bridges that continue component c, at value n, using components in l
  pass


# main

# get starting 0 points
starting_points = getStartingPoints(0, components) # component : list

for c,l in starting_points.items():
  print(c + ': ' + str(l)) # starting component : remaining list


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')