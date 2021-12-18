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

def target_hit(x,y):
  (sx,sy) = 0,0 # start pos
  #print(str(sx) + ',' + str(sy) + ',' + str(x))
  maxsy = -1
  prev_x = 0
  prev_y = 0

  drag = 0
  if x > 0:
    drag = -1
  else:
    drag = 1

  while True:
    #print(str(sx) + ',' + str(sy) + ',' + str(x))
    sx = sx + x
    sy = sy + y

    # apply drag
    # Due to drag, the probe's x velocity changes by 1 toward the value 0;
    # that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0,
    # or does not change if it is already 0.
    if x != 0:
      x = x + drag
    
    # apply gravity
    y = y - 1

    if sy > maxsy:
      maxsy = sy

    if within_target_area(sy,sx):
      #print(str(sx) + ',' + str(sy) + ',' + str(x))
      return (True, maxsy)
    
    if sy < miny:
      return (False, maxsy)

    prev_y = sy
    prev_x = sx
    
    """
    if sx > maxx:
      return (False, maxsy)
    
    if sx < minx and sy < miny:
      return (False, maxsy)
    """


# TEST
#target_hit(6,9) # BAD
#target_hit(7,2) # GOOD
#sys.exit()


"""
(hit, height) = target_hit(6,9)
print(hit)
print(height)
"""
count = 0
max_height = -99
d = {}
for x in range(0,500):
  for y in range(-500,1000):
    (hit, height) = target_hit(x,y)
    if hit:
      count += 1
      d [ str(x)+','+str(y) ] = 0
      """
      if height > max_height:
        max_height = height
        the_y = y
        the_x = x
      """

print(len(d))

# 4616 too high
# 1998 wrong
# 1964 too low
# 802 too low
# 4031 wrong


"""
target area: x=20..30, y=-10..-5

target area: x=32..65, y=-255..-177


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
