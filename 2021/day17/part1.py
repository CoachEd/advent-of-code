"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())
arr = l[0][13:].replace(',','').replace('..',',').split()
arr[0] = arr[0][2:]
arr[1] = arr[1][2:]
arr2 = arr[0].split(',')
arr3 = arr[1].split(',')

# target area
minx = int(arr2[0])
maxx = int(arr2[1])
miny = int(arr3[0])
maxy = int(arr3[1])

def within_target_area(y,x):
  global minx
  global miny
  global maxx
  global maxy
  if x >= minx and x <= maxx and y >= miny and y <= maxy:
    return True
  return False

(sx,sy) = 0,0 # start pos
(x,y) = 7,2 # initial velocity

#print(str(sy) + ',' + str(sx))
while True:
  sx = sx + x
  sy = sy + y
  if x > 0:
    x = x - 1
  elif x < 0:
    x = x + 1
  y = y - 1
  #print(str(sy) + ',' + str(sx))
  if within_target_area(sy,sx):
    print('hit: y,x: ' + str(sy) + ',' + str(sx))
    break
  elif sy < miny:
    print('miss')
    break
  elif sx > maxx:
    print('miss')
    break
  elif sx < minx and sy < miny:
    print('miss')
    break
  
  
"""
.............#....#............
.......#..............#........
...............................
S........................#.....
...............................
...............................
...........................#...
...............................
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTT#TT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
"""




print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
