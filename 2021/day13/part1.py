# part 1


"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

def fold(a, axis, n):
  newarr = []
  if axis == 'y':
    y0 = n
    for y1 in range(n+1, len(a)):
      y0 = y0 - 1
      if y0 < 0:
        break
      for x in range(0, len(a[y1])):
        c = a[y1][x]
        if c == '#':
          a[y0][x] = c
    for y in range(0,n):
      newarr.append(a[y])
  else:
    for y in range(0, len(a)):
      x0 = n
      for x1 in range(n+1,len(a[y])):
        x0 = x0 - 1
        if x0 < 0:
          break
        c = a[y][x1]
        if c == '#':
          a[y][x0] = c
    for y in range(0, len(a)):
      arr1 = []
      for x in range(0,n):
        arr1.append(a[y][x])
      newarr.append(arr1)
  return newarr

def printpaper(a):
  s = ''
  for r in a:
    for e in r:
      s += e
    s += '\n'
  print(s)

def countdots(a):
  n = 0
  for r in a:
    for e in r:
      if e == '#':
        n += 1
  return n

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

coords = []
idx = -1
maxx = -1
maxy = -1
for s in l:
  idx += 1
  if s == '':
    break
  arr = s.split(',')
  x = int(arr[0])
  y = int(arr[1])
  coords.append([x,y])
  if x > maxx:
    maxx = x
  if y > maxy:
    maxy = y

folds = []
for i in range(idx+1, len(l)):
  arr1 = l[i].split(' ')
  arr2 = arr1[2].split('=')
  d = arr2[0]
  n = int(arr2[1])
  folds.append([d,n])

paper = [[ '.' for x in range(maxx+1)] for y in range(maxy+1)]

for c in coords:
  x = c[0]
  y = c[1]
  paper[y][x] = '#'

paper = fold(paper, folds[0][0], folds[0][1])
#paper = fold(paper, folds[1][0], folds[1][1])

print(countdots(paper))
#printpaper(paper)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')

