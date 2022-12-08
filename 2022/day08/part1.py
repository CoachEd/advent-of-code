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
#printArr(arr, 1)

count = 0
for r in range(len(arr)):
  for c in range(len(arr[r])):
    if arr[r][c][1] or  arr[r][c][2] or  arr[r][c][3] or  arr[r][c][4]:
      count += 1
print(count)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')