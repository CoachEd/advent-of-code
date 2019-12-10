import sys
import time
import math
from copy import copy, deepcopy

def printArr(a):
  s = ''
  for y in range(len(a)):
    for x in range(len(a[y])):
      s = s + a[y][x]
    s = s + '\n'
  print(s)

def validIndex(x,y,arr):
  max_y = len(arr) - 1
  max_x = len(arr[0]) - 1
  if x < 0 or y < 0:
    return False
  if y > max_y or x > max_x:
    return False
  return True

print()
start_secs = time.time()

spacemap =""".#..#
.....
#####
....#
...##
"""

# create the original 2D array
origarr = []
arr = spacemap.split('\n')[:-1]
for y in range(len(arr)):
  temparr = []
  for x in range(len(arr[y])):
    temparr.append(arr[y][x])
  origarr.append(temparr)

# main loop
for y in range(len(origarr)):
  for x in range(len(origarr[y])):
    if origarr[y][x] == '#':
      # found an steroid at y,x, process it
      arr2 = deepcopy(origarr)
      #y,x is me, remove it from the temp arr, so we don't process it later
      arr2[y][x] = '.'

      # remove all but first one going outwards from me, going UP
      # me
      y1 = y
      x1 = x
      found = False
      while(True):
        y1 = y1 - 1 # go UP
        if validIndex(x1,y1,arr2):
          if arr2[y1][x1] == '#':
            if not found:
              # we found the first one, leave it
              found = True
            else:
              # remove all others
              arr2[y1][x1] = '.'
        else:
          # went too far
          break

      # remove all but first one going outwards from me, going DOWN
      # me
      y1 = y
      x1 = x
      found = False
      while(True):
        y1 = y1 + 1 # go DOWN
        if validIndex(x1,y1,arr2):
          if arr2[y1][x1] == '#':
            if not found:
              # we found the first one, leave it
              found = True
            else:
              # remove all others
              arr2[y1][x1] = '.'
        else:
          # went too far
          break

      # remove all but first one going outwards from me, going RIGHT
      # me
      y1 = y
      x1 = x
      found = False
      while(True):
        x1 = x1 + 1 # go RIGHT
        if validIndex(x1,y1,arr2):
          if arr2[y1][x1] == '#':
            if not found:
              # we found the first one, leave it
              found = True
            else:
              # remove all others
              arr2[y1][x1] = '.'
        else:
          # went too far
          break
      
      # remove all but first one going outwards from me, going LEFT
      # me
      y1 = y
      x1 = x
      found = False
      while(True):
        x1 = x1 - 1 # go LEFT
        if validIndex(x1,y1,arr2):
          if arr2[y1][x1] == '#':
            if not found:
              # we found the first one, leave it
              found = True
            else:
              # remove all others
              arr2[y1][x1] = '.'
        else:
          # went too far
          break

      # remove all but first one going outwards from me, moving TOP RIGHT
      # me
      y1 = y
      x1 = x
      found = False
      while(True):
        x1 = x1 + 1 # move TOP RIGHT
        y1 = y1 - 1
        if validIndex(x1,y1,arr2):
          if arr2[y1][x1] == '#':
            if not found:
              # we found the first one, leave it
              found = True
            else:
              # remove all others
              arr2[y1][x1] = '.'
        else:
          # went too far
          break

      # remove all but first one going outwards from me, moving BOTTOM RIGHT
      # me
      y1 = y
      x1 = x
      found = False
      while(True):
        x1 = x1 + 1 # move BOTTOM RIGHT
        y1 = y1 + 1
        if validIndex(x1,y1,arr2):
          if arr2[y1][x1] == '#':
            if not found:
              # we found the first one, leave it
              found = True
            else:
              # remove all others
              arr2[y1][x1] = '.'
        else:
          # went too far
          break

      # remove all but first one going outwards from me, moving TOP LEFT
      # me
      y1 = y
      x1 = x
      found = False
      while(True):
        x1 = x1 - 1 # move TOP LEFT
        y1 = y1 - 1
        if validIndex(x1,y1,arr2):
          if arr2[y1][x1] == '#':
            if not found:
              # we found the first one, leave it
              found = True
            else:
              # remove all others
              arr2[y1][x1] = '.'
        else:
          # went too far
          break

      # remove all but first one going outwards from me, moving BOTTOM LEFT
      # me
      y1 = y
      x1 = x
      found = False
      while(True):
        x1 = x1 - 1 # move BOTTOM LEFT
        y1 = y1 + 1
        if validIndex(x1,y1,arr2):
          if arr2[y1][x1] == '#':
            if not found:
              # we found the first one, leave it
              found = True
            else:
              # remove all others
              arr2[y1][x1] = '.'
        else:
          # went too far
          break

      # now loop through remaining #s, get the offset angles, and do the same thing as above
      # TODO
      




      




"""
for origin x,y:
Reduce: Remove up,down,left,right,tr,tl,br,bl, all but first one found, change that first one to a different character

for each x,y:
  if it is a "#" and not the origin:
  Start at curr(0,0)
  find cx and cy offset to origin(ox,oy): 
    offsetx = cx - ox
    offsety = cy - oy

  get gcd of offsetx and offsety
  reduce offsetx and offsety by gcd
  from origin, traverse to offsetx and offsety, removing all but the first one. change that first char to something else

count how many satellites remain

"""




print( math.gcd(0,4) )



end_secs = time.time()
print('elapsed time: ' + str(end_secs - start_secs) + ' seconds')
