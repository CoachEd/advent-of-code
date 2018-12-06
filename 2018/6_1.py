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

cols = 347
rows = 352


grid = [grid[:] for grid in [['.'] * cols] * rows] 


c = [
[181, 184],
[230, 153],
[215, 179],
[84, 274],
[294, 274],
[127, 259],
[207, 296],
[76, 54],
[187, 53],
[318, 307],
[213, 101],
[111, 71],
[310, 295],
[40, 140],
[176, 265],
[98, 261],
[315, 234],
[106, 57],
[40, 188],
[132, 292],
[132, 312],
[97, 334],
[292, 293],
[124, 65],
[224, 322],
[257, 162],
[266, 261],
[116, 122],
[80, 319],
[271, 326],
[278, 231],
[191, 115],
[277, 184],
[329, 351],
[58, 155],
[193, 147],
[45, 68],
[310, 237],
[171, 132],
[234, 152],
[158, 189],
[212, 100],
[346, 225],
[257, 159],
[330, 112],
[204, 320],
[199, 348],
[207, 189],
[130, 289],
[264, 223]
  ]

namestr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwx"
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

    s1 = 10000000000000000000000
    i1 = -1
    for j in range(len(l)):
      if l[j] < s1:
        s1 = l[j]
        i1 = j
    
    s2 = 10000000000000000000000
    i2 = -1
    for j in range(len(l)):
      if l[j] < s2 and j != i1:
        s2 = l[j]
        i2 = j

    if (s1 < s2):
      grid[row][col] = namestr[i1]
      
#printGrid(grid)

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


#prev
#['k', 'H', 'R', 'X', 'I', 's', 'N', 'S', 'D', 'c', 'V', 'U', 'u', 'd', 'h']
#x: 6738













 

    
