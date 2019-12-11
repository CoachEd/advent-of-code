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

spacemap ="""###..#.##.####.##..###.#.#..
#..#..###..#.......####.....
#.###.#.##..###.##..#.###.#.
..#.##..##...#.#.###.##.####
.#.##..####...####.###.##...
##...###.#.##.##..###..#..#.
.##..###...#....###.....##.#
#..##...#..#.##..####.....#.
.#..#.######.#..#..####....#
#.##.##......#..#..####.##..
##...#....#.#.##.#..#...##.#
##.####.###...#.##........##
......##.....#.###.##.#.#..#
.###..#####.#..#...#...#.###
..##.###..##.#.##.#.##......
......##.#.#....#..##.#.####
...##..#.#.#.....##.###...##
.#.#..#.#....##..##.#..#.#..
...#..###..##.####.#...#..##
#.#......#.#..##..#...#.#..#
..#.##.#......#.##...#..#.##
#.##..#....#...#.##..#..#..#
#..#.#.#.##..#..#.#.#...##..
.#...#.........#..#....#.#.#
..####.#..#..##.####.#.##.##
.#.######......##..#.#.##.#.
.#....####....###.#.#.#.####
....####...##.#.#...#..#.##.
"""

# create the original 2D array
origarr = []
arr = spacemap.split('\n')[:-1]
for y in range(len(arr)):
  temparr = []
  for x in range(len(arr[y])):
    temparr.append(arr[y][x])
  origarr.append(temparr)

#printArr(origarr)

# main loop
directions = ['up','topright','right','bottomright','down','bottomleft','left','topleft']
max_points = -1
keep_x = -1
keep_y = -1
for y in range(len(origarr)):
  for x in range(len(origarr[y])):

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
      slope = 0
    else:
      slope = abs((keep_y - y) / denom)
      slope = "{:15.6f} ".format(float(slope))

    tslopes.append(str(slope))
  slopes.append(tslopes)
slopes[keep_y][keep_x] =  ' **** '

points = []






origcount = -1
while not (origcount == countArr(origarr)):
  origcount = countArr(origarr)

  # one rotation

  # remove UP
  x = keep_x
  y = keep_y
  found = False
  while not found:
    y = y - 1
    if validIndex(x,y,origarr):
      if origarr[y][x] == '#':
        found = True
        points.append([x,y])
        origarr[y][x] = '.'
    else:
      break

  # remove topright quadrant
  dict1 = {}
  for y in range(0,keep_y):
    for x in range(keep_x+1,len(origarr[y])):
      if origarr[y][x] == '#':
        if slopes[y][x] in dict1.values():
          key = list(dict1.keys())[list(dict1.values()).index(slopes[y][x])]
          tarr = key.split(',')
          tx = int(tarr[1])
          ty = int(tarr[0])
          tdist = abs(keep_x-tx) + abs(keep_y-ty)
          ndist = abs(keep_x-x) + abs(keep_y-y)
          if ndist < tdist:
            # replace
            del dict1[key]
            key = str(y) + ',' + str(x)
            dict1[key] = slopes[y][x]
        else:
          key = str(y) + ',' + str(x)
          dict1[key] = slopes[y][x]
  #sort dictionary by values
  dict1 = {k: v for k, v in sorted(dict1.items(), key=lambda item: item[1],reverse=True)}
  for k,v in dict1.items():
    tarr = k.split(',')
    tx = int(tarr[1])
    ty = int(tarr[0])
    origarr[ty][tx] = '.'
    points.append([tx,ty])

  # remove RIGHT
  x = keep_x
  y = keep_y
  found = False
  while not found:
    x = x + 1
    if validIndex(x,y,origarr):
      if origarr[y][x] == '#':
        found = True
        points.append([x,y])
        origarr[y][x] = '.'
    else:
      break

  # remove bottom right quadrant
  dict1 = {}
  for y in range(keep_y+1,len(origarr)):
    for x in range(keep_x+1,len(origarr[y])):
      if origarr[y][x] == '#':
        if slopes[y][x] in dict1.values():
          key = list(dict1.keys())[list(dict1.values()).index(slopes[y][x])]
          tarr = key.split(',')
          tx = int(tarr[1])
          ty = int(tarr[0])
          tdist = abs(keep_x-tx) + abs(keep_y-ty)
          ndist = abs(keep_x-x) + abs(keep_y-y)
          if ndist < tdist:
            # replace
            del dict1[key]
            key = str(y) + ',' + str(x)
            dict1[key] = slopes[y][x]
        else:
          key = str(y) + ',' + str(x)
          dict1[key] = slopes[y][x]
  #sort dictionary by values
  dict1 = {k: v for k, v in sorted(dict1.items(), key=lambda item: item[1])}
  for k,v in dict1.items():
    tarr = k.split(',')
    tx = int(tarr[1])
    ty = int(tarr[0])
    origarr[ty][tx] = '.'
    points.append([tx,ty])

  # remove DOWN
  x = keep_x
  y = keep_y
  found = False
  while not found:
    y = y + 1
    if validIndex(x,y,origarr):
      if origarr[y][x] == '#':
        found = True
        points.append([x,y])
        origarr[y][x] = '.'
    else:
      break

  # remove bottom left quadrant
  dict1 = {}
  for y in range(keep_y+1,len(origarr)):
    for x in range(0,keep_x):
      if origarr[y][x] == '#':
        if slopes[y][x] in dict1.values():
          key = list(dict1.keys())[list(dict1.values()).index(slopes[y][x])]
          tarr = key.split(',')
          tx = int(tarr[1])
          ty = int(tarr[0])
          tdist = abs(keep_x-tx) + abs(keep_y-ty)
          ndist = abs(keep_x-x) + abs(keep_y-y)
          if ndist < tdist:
            # replace
            del dict1[key]
            key = str(y) + ',' + str(x)
            dict1[key] = slopes[y][x]
        else:
          key = str(y) + ',' + str(x)
          dict1[key] = slopes[y][x]
  #sort dictionary by values
  dict1 = {k: v for k, v in sorted(dict1.items(), key=lambda item: item[1],reverse=True)}
  for k,v in dict1.items():
    tarr = k.split(',')
    tx = int(tarr[1])
    ty = int(tarr[0])
    origarr[ty][tx] = '.'
    points.append([tx,ty])  

  # remove LEFT
  x = keep_x
  y = keep_y
  found = False
  while not found:
    x = x - 1
    if validIndex(x,y,origarr):
      if origarr[y][x] == '#':
        found = True
        points.append([x,y])
        origarr[y][x] = '.'
    else:
      break

  # remove top left quadrant
  dict1 = {}
  for y in range(0,keep_y):
    for x in range(0,keep_x):
      if origarr[y][x] == '#':
        if slopes[y][x] in dict1.values():
          key = list(dict1.keys())[list(dict1.values()).index(slopes[y][x])]
          tarr = key.split(',')
          tx = int(tarr[1])
          ty = int(tarr[0])
          tdist = abs(keep_x-tx) + abs(keep_y-ty)
          ndist = abs(keep_x-x) + abs(keep_y-y)
          if ndist < tdist:
            # replace
            del dict1[key]
            key = str(y) + ',' + str(x)
            dict1[key] = slopes[y][x]
        else:
          key = str(y) + ',' + str(x)
          dict1[key] = slopes[y][x]
  #sort dictionary by values
  dict1 = {k: v for k, v in sorted(dict1.items(), key=lambda item: item[1])}
  for k,v in dict1.items():
    tarr = k.split(',')
    tx = int(tarr[1])
    ty = int(tarr[0])
    origarr[ty][tx] = '.'
    points.append([tx,ty])  



"""
what do you get if you multiply its (200th asteroid) X coordinate by 100 and then add its Y coordinate? 
"""
asteroid200 = points[199]
answer = int(asteroid200[0]) * 100 + (asteroid200[1])
print(answer)
#num = 1
#for p in points:
#  print(str(num) + ' x,y: ' + str(p[0]) + ',' + str(p[1]))
#  num = num + 1



end_secs = time.time()
print('elapsed time: ' + str(end_secs - start_secs) + ' seconds')
