
# Day 9 part 2
import time
import sys
import math
from copy import copy, deepcopy
start_secs = time.time()
print('')
 
# SOLUTION
# read in input file

def printm(m):
  global rows,cols
  s = ''
  for y in range(rows):
    for x in range(cols):
      if m[y][x] != None:
        s += str(m[y][x])
      s += ' '
    s += '\n'
  print(s)

l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

n = len(l[0].split())
cols = n * 2 + 1
rows = n
m = [ [None for i in range(cols)] for j in range(rows) ]

tot = 0
for s in l:
  # [0, 3, 6, 9, 12, 15]
  a = [int(x) for x in s.split()]
  a.reverse()
  
  # add top row
  i = 0
  for x in range(0, cols, 2):
    if i < len(a):
      m[0][x] = a[i]
    i += 1
    
  # go down
  lastrowi = None
  for y in range(1,rows):
    n2 = n - y
    lastrowi = y
    allzeroes = True
    for x in range(y,cols,2):
      if n2 > 0:
        m[y][x] = m[y-1][x-1] - m[y-1][x+1]
        if m[y][x] != 0:
          allzeroes = False
      n2 -= 1
    if allzeroes:
      break
  
  # up
  for y in range(lastrowi,-1,-1):
    n2 = n - y
    if y == lastrowi:
      m[y][n2 * 2 + y] = 0
    else:
      m[y][n2 * 2 + y] = m[y][n2 * 2 + y - 2] - m[y+1][n2 * 2 + y - 1]
    if y == 0:
      tot += m[y][n2 * 2 + y]

#printm(m)
print(tot)

# 1909851346 too high
print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')