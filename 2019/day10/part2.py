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

def countArr(a):
  sum = 0
  for y in range(len(a)):
    for x in range(len(a[y])):
      if a[y][x] == '#':
        sum = sum + 1
  return sum

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

spacemap =""".#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....#...###..
..#.#.....#....##
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
directions = ['up','down','right','left','topright','bottomright','topleft','bottomleft']
max_points = -1
keep_x = -1
keep_y = -1
for y in range(len(origarr)):
  for x in range(len(origarr[y])):

    #TEST
    #if not (y == 0 and x == 0):
    #  continue

    if origarr[y][x] == '#':
      # found an asteroid at y,x, process it
      arr2 = deepcopy(origarr)
      #y,x is me, remove it from the temp arr, so we don't process it later
      arr2[y][x] = '.'

      # remove all but first one that we're going for in directions
      for direction in directions:

        # me
        y1 = y
        x1 = x
        found = False
        while(True):

          if direction == 'up':
            y1 = y1 - 1
          elif direction == 'down':
            y1 = y1 + 1 
          elif direction == 'right':
            x1 = x1 + 1
          elif direction == 'left':
            x1 = x1 - 1 
          elif direction == 'topright':
            x1 = x1 + 1 
            y1 = y1 - 1
          elif direction == 'bottomright':
            x1 = x1 + 1 
            y1 = y1 + 1
          elif direction == 'topleft':
            x1 = x1 - 1 
            y1 = y1 - 1
          elif direction == 'bottomleft':
            x1 = x1 - 1 
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
      for y2 in range(len(origarr)):
        for x2 in range(len(origarr[y])):
          if y2 == y and x2 == x:
            continue

          offsety = y2 - y
          offsetx = x2 - x
          xygcd = math.gcd(offsety,offsetx)
          offsety = offsety / xygcd
          offsetx = offsetx / xygcd
          y1 = y
          x1 = x
          found = False          
          while(True):
            x1 = int(x1 + offsetx)
            y1 = int(y1 + offsety)
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

      #printArr(arr2)
      n = countArr(arr2)
      if (n > max_points):
        max_points = n
        keep_x = x
        keep_y = y

print(str(max_points) + ' from y,x ' + str(keep_y) + ',' + str(keep_x))        

# part 2
slopes = []
for y in range(len(origarr)):
  tslopes = []
  for x in range(len(origarr[y])):

    denom = keep_x - x
    if denom == 0:
      m = " {:5.2f} ".format(float(0))
    else:
      m = abs((keep_y -y) / (keep_x - x))
      m = " {:5.2f} ".format(float(m))

    tslopes.append(str(m))

  slopes.append(tslopes)
slopes[keep_y][keep_x] = '  **** '
printArr(slopes)

end_secs = time.time()
print('elapsed time: ' + str(end_secs - start_secs) + ' seconds')
