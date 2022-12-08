import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

def printArr(a,i):
  s = ''
  for r in range(len(a)):
    for c in range(len(a[r])):
      s += str(a[r][c][i])[0:1]
    s += '\n'
  print(s)

def printArr2(a,i):
  s = ''
  for r in range(len(a)):
    for c in range(len(a[r])):
      s += str(a[r][c][i])
    s += '\n'
  print(s)

def rightVis(a):
  for row in a:
    maxR = -1
    for c in range(len(row)-1, 0, -1):
      if (row[c][0] > maxR):
        maxR = row[c][0]
      for c2 in range(c-1, -1, -1):
        if row[c2][0] > maxR:
          row[c2][1] = True
          maxR = row[c2][0]

def leftVis(a):
  for row in a:
    maxR = -1
    for c in range(0, len(row)-1):
      if (row[c][0] > maxR):
        maxR = row[c][0]
      for c2 in range(c+1, len(row)):
        if row[c2][0] > maxR:
          row[c2][2] = True
          maxR = row[c2][0] 
      
def topVis(a):
  for c in range(0, len(a[0])):
    maxR = -1
    for r in range(0, len(a)-1):
      if (a[r][c][0] > maxR):
        maxR = a[r][c][0]
      for r2 in range(r+1, len(a)):
        if a[r2][c][0] > maxR:
          a[r2][c][3] = True
          maxR = a[r2][c][0]

def botVis(a):
  for c in range(0, len(a[0])):
    maxR = -1
    for r in range(len(a)-1, 0, -1):
      if (a[r][c][0] > maxR):
        maxR = a[r][c][0]
      for r2 in range(r-1, -1, -1):
        if a[r2][c][0] > maxR:
          a[r2][c][4] = True
          maxR = a[r2][c][0]

# SOLUTION
# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

rows,cols = len(l),len(l[0])

arr = [[0 for x in range(cols)] for y in range(rows)] 
for r in range(rows):
  for c in range(cols):
    visFromR = False
    visFromL = False
    visFromT = False
    visFromB = False
    if r == 0:
      visFromT = True
    if r == rows - 1:
      visFromB = True
    if c == 0:
      visFromL = True
    if c == cols - 1:
      visFromR = True

    arr[r][c] = [ int(l[r][c]), visFromR, visFromL, visFromT, visFromB ]


rightVis(arr)
leftVis(arr)
topVis(arr)
botVis(arr)
#printArr(arr, 4)

# element: # right view, left view, top view, bottom view
arr2 = [[ [0,0,0,0] for x in range(cols)] for y in range(rows)] 

# right viewing distance
for r in range(rows):
  for c in range(0, cols-1):
    if arr[r][c][1]:
      # visible from right
      arr2[r][c][0] = cols - c - 1
    else:
      x = 0
      for k in range(c+1, cols):
        x += 1
        if arr[r][k][0] >= arr[r][c][0]:
          break
      arr2[r][c][0] = x

# left viewing distance
for r in range(rows):
  for c in range(1, cols):
    if arr[r][c][2]:
      # visible from left
      arr2[r][c][1] = c
    else:
      x = 0
      for k in range(c-1, -1, -1):
        x += 1
        if arr[r][k][0] >= arr[r][c][0]:
          break
      arr2[r][c][1] = x        

# top viewing distance
for c in range(cols):
  for r in range(1, rows):
    if arr[r][c][3]:
      # visible from top
      arr2[r][c][2] = r
    else:
      x = 0
      for k in range(r-1, -1, -1):
        x += 1
        if arr[k][c][0] >= arr[r][c][0]:
          break
      arr2[r][c][2] = x 

# bot viewing distance
for c in range(cols):
  for r in range(rows - 2, -1, -1):
    if arr[r][c][4]:
      # visible from bot
      arr2[r][c][3] = rows - r - 1
      pass
    else:
      x = 0
      for k in range(r+1, rows):
        x += 1
        if arr[k][c][0] >= arr[r][c][0]:
          break
      arr2[r][c][3] = x

max_scenic_score = -1
for r in range(rows):
  for c in range(cols):
    # right view, left view, top view, bottom view
    scenic_score = arr2[r][c][0] * arr2[r][c][1] * arr2[r][c][2] * arr2[r][c][3]
    if scenic_score > max_scenic_score:
      max_scenic_score = scenic_score

print(max_scenic_score)
# 133560 TOO LOW
# 1672704 TOO HIGH


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')