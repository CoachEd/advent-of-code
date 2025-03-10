
# part 2
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

# 128,487 -> 128,246

rows = 1000
cols = 1000
m = [[ 0 for col in range(cols)] for row in range(rows)]
mylines = []
for line in l:
  arr = line.split('->')
  s1 = arr[0].strip()
  s2 = arr[1].strip()
  arr = s1.split(',')
  x1 = int(arr[0])
  y1 = int(arr[1])
  arr = s2.split(',')
  x2 = int(arr[0])
  y2 = int(arr[1])
  mylines.append([x1,y1,x2,y2])

for line in mylines:
  x1 = line[0]
  y1 = line[1]
  x2 = line[2]
  y2 = line[3]
  xf = -1 if (x1 > x2) else 1
  yf = -1 if (y1 > y2) else 1

  slope = 0
  
  # 8,0 0,8
  if (x2-x1) != 0:
    slope = abs((y2-y1)/(x2-x1))
  
  if x1 == y1 and x2 == y2:
    if x1 > x2:
      for x in range(x1,y2-1,-1):
        m[x][x] += 1
    else:
      for x in range(x1,y2+1,1):
        m[x][x] += 1
  elif slope == 1:
      # 6,4 2,0
      xf = 1
      yf = 1
      if x1 > x2:
        xf = -1
      if y1 > y2:
        yf = -1
      cnt = abs(x1-x2)+1
      x = x1
      y = y1
      for i in range(cnt):
        m[y][x] += 1
        x += xf
        y += yf
  elif x1 == x2:
    # vert
    for y in range(y1, y2+yf,
                  yf):
      m[y][x1] += 1
  elif y1 == y2:
    # horiz
    for x in range(x1, x2+xf,
                  xf):
      m[y1][x] += 1

count = 0
for row in m:
  for e in row:
    if e >= 2:
      count += 1

print('done')
print(count)

# 97576
# 5553



  

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')