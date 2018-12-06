import cProfile
import math

# enable profiling
#pr = cProfile.Profile()
#pr.enable()

def printGrid(g):
  s = ''
  for r in range(len(g)):
    for c in range(len(g[r])):
      s = s + g[r][c]
    s = s + '\n'
  print(s)

def dist(x1,y1,x2,y2):
  return abs(x1-x2) + abs(y1-y2)


print("start...")

# max coords 346 , 351

cols = 10
rows = 10

grid = [grid[:] for grid in [['.'] * cols] * rows] 


c = [
[1, 1],
[1, 6],
[8, 3],
[3, 4],
[5, 5],
[8, 9]
  ]

namestr = "ABCDEF"
for i in range(len(c)):
  grid[c[i][1]][c[i][0]] = namestr[i]

#printGrid(grid)

for row in range(len(grid)):
  for col in range(len(grid[row])):
    if grid[row][col] != '.':
      continue
    l = [0] * len(c)
    for i in range(len(c)):
      d = dist(c[i][1],c[i][0],row,col)
      l[i] = d

    s1 = 10000000000
    i1 = -1
    for j in range(len(l)):
      if l[j] < s1:
        s1 = l[j]
        i1 = j
    
    s2 = 10000000000
    i2 = -1
    for j in range(len(l)):
      if l[j] < s2 and j != i1:
        s2 = l[j]
        i2 = j

    if (s1 < s2):
      grid[row][col] = namestr[i1].lower()
      
printGrid(grid)

counts = [0] * len(namestr)
for row in range(len(grid)):
  for col in range(len(grid[row])):
    thec = grid[row][col]
    thei = namestr.find(thec)
    counts[thei] = counts[thei] + 1

# find infite areas
iarr = []
for row in range(len(grid)):
  for col in range(len(grid[row])):
    if grid[row][col] != '.':
      if row == 0 or col == 0 or row ==(rows-1) or cols == (cols-1):
        if grid[row][col] not in iarr:
          iarr.append(grid[row][col])      
print(iarr)

largest = 0
largesti = -1
for i in range(len(counts)):
  if counts[i] > largest and namestr[i] not in iarr:
    largest = counts[i]
    largesti = i

print(namestr[largesti] + ": " + str(largest))
      
print("done.")

#pr.disable()
#pr.print_stats()
















 

    
