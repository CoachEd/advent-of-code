import time
import sys
from copy import copy, deepcopy

# read in input file
my_file = open("inp2.txt", "r", encoding='utf-8')
lines = my_file.readlines()
l=[None for i in range(len(lines))]
for i in range(len(lines)):
  l[i] = lines[i].strip()

def printmap(m):
  s = ''
  for y in range(len(m)):
    for x in range(len(m[y])):
      s += m[y][x]
    s += '\n'
  print(s)

def dist(p1,p2):
  (y0,x0) = p1
  (y1,x1) = p2
  return abs(y0 - y1) + abs(x0 - x1)

# SOLUTION START - start timing
start_secs = time.time()

"""
rows = len(l) * 5
cols = len(l[0]) * 5
cy = int(rows / 2)
cx = int(cols / 2)
offset = int(len(l) / 2)
y0 = cy - offset
x0 = cx - offset
"""
galaxies = []

orig_rows = len(l)
orig_cols = len(l[0])
m = [ ['.' for x in range(orig_cols) ] for y in range(orig_rows) ]

# populate
for y in range(orig_rows):
  for x in range(orig_cols):
    m[y][x] = l[y][x]
    if m[y][x] == '#':
      galaxies.append((y,x))

empty_rows = []
for y in range(1,orig_rows-1):
  if not '#' in m[y]:
    empty_rows.append(y)

empty_cols = []
for x in range(1,orig_cols-1):
  is_empty = True
  for y in range(orig_rows):
    if m[y][x] == '#':
      is_empty = False
      break
  if is_empty:
    empty_cols.append(x)

print((empty_rows,empty_cols))
print(galaxies)

# insert rows
m2 = []
for y in range(orig_rows):
  m2.append(m[y])
  if y in empty_rows:
    m2.append(m[y].copy())
m = m2

# insert cols
# TODO: 

printmap(m)
sys.exit()


m2 = [ ['.' for x in range(orig_cols*2)] for y in range(orig_rows*2)]
offsety = 2
offsetx = 2
gnum = 1
for i in range(len(galaxies)):
  (y,x) = (galaxies[i])
  y += offsety
  x += offsetx
  m2[y][x] = str(gnum)
  galaxies[i] = (y,x)
  gnum += 1
print(galaxies)
sys.exit()
  
printmap(m2)
print(galaxies)



"""
galaxies = []
for y in range(len(m2)):
  for x in range(len(m2[y])):
    if m2[y][x].isdigit():
      galaxies.append((y,x))
print(galaxies)
"""

tot = 0
for i in range(len(galaxies)-1):
  for j in range(i+1, len(galaxies)):
    d = dist(galaxies[i],galaxies[j])
    print((galaxies[i],galaxies[j],d))
    tot += d
print(tot)



end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
# SOLUTION END - stop timing