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

def getBridges(c, n, l):
  # TODO
  # get the bridges that continue component c, at value n, using components in l
  pass


# main

# get starting points
starting_points = {} # component : list
for c in components:
  (x,y) = getEnds(c)
  if x == 0 or y == 0:
    arr1 = components.copy()
    arr1.remove(c)
    starting_points[c] = arr1

for c,l in starting_points.items():
  print(c + ': ' + str(l)) # starting component : remaining list


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')