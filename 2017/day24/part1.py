import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

# SOLUTION
# read in input file
components=[]
max_strength = 0
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  components.append(line.strip())

def getEnds(s):
  a = s.split('/')
  return (int(a[0]), int(a[1]))

def calcStrength(a):
  n = 0
  for c in a:
    (x,y) = getEnds(c)
    n += x + y
  return n

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

def getBridges(c, n, l, fl):
  global max_strength
  # TODO
  # get the bridges that continue component c, at value n, using components in l
  # fl is the final list being passed down
  #fl.append(c)
  next_points = getStartingPoints(n, l)
  if len(next_points) == 0:
    # no other bridges possible
    s1 = calcStrength(fl)
    if s1 > max_strength:
      max_strength = s1
    return
  for c2,l2 in next_points.items():
    (x,y) = getEnds(c2)
    n2 = x
    if x == n:
      n2 = y
    fl2 = fl.copy()
    fl2.append(c2)
    getBridges(c2, n2, l2, fl2)
      
# main

# get starting 0 points
starting_points = getStartingPoints(0, components) # component : list

for c,l in starting_points.items():
  #print(c + ': ' + str(l)) # starting component : remaining list
  (x,y) = getEnds(c)
  if x == 0:
    n = y
  else:
    n = x
  getBridges(c, n, l, [c])

print(max_strength)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')