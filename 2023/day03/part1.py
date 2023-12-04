
import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')
 
# SOLUTION

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
cols = len(lines[0].strip())
rows = len(lines)

a = [[0 for x in range(cols)] for y in range(rows)]

def isValid(x,y):
  global a,cols,rows
  if x < 0 or y < 0 or x >= cols or y >= rows:
    return False
  else:
    return True
  
def bySymbol(x,y):
  global a
  (tlX,tlY) = (x-1,y-1)
  (tX,tY) = (x,y-1)
  (trX,trY) = (x+1,y-1)
  (lX,lY) = (x-1,y)
  (rX,rY) = (x+1,y)
  (blX,blY) = (x-1,y+1)
  (bX,bY) = (x,y+1)
  (brX,brY) = (x+1,y+1)
  a2 = [[tlX,tlY],[tX,tY],[trX,trY],[lX,lY],[rX,rY],[blX,blY],[bX,bY],[brX,brY]]
  for p in a2:
    (x0,y0) = (p[0],p[1])
    if isValid(x0,y0) and not a[y0][x0].isdigit() and a[y0][x0] != '.':
      return True
  return False



y = -1
for line in lines:
  y += 1
  line = line.strip()
  for x in range(cols):
    a[y][x] = line[x]

tot = 0
for y in range(rows):
  num = ''
  found = False
  for x in range(cols):
    c = a[y][x]
    if c.isdigit():
      num += c
      if bySymbol(x,y):
        found = True
      (crx,cry) = (x+1,y)
      if (not isValid(crx,cry) or not a[cry][crx].isdigit()):
        if found:
          #print(num)
          tot += int(num)
          num = ''
          found = False
        else:
          num = ''
          found = False
        
        
print()
print(tot)
# 96791501819 too high


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
