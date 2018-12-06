import cProfile
import math

# enable profiling
#pr = cProfile.Profile()
#pr.enable()

def valid(x,y,rows,cols):
  return (x >= 0 and y >= 0 and x < rows and y < cols)

def printGrid(g):
  s = ''
  for r in range(len(g)):
    for c in range(len(g[r])):
      s = s + g[r][c]
    s = s + '\n'
  print(s)

def dist(x1,y1,x2,y2):
  return (abs(x1-x2) + abs(y1-y2))


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


# sample data
#c = [
#[1, 1],
#[1, 6],
#[8, 3],
#[3, 4],
#[5, 5],
#[8, 9]
#]
#namestr = "ABCDEF"
#cols = 10 
#rows = 10 
#grid = [grid[:] for grid in [['.'] * cols] * rows] 


for i in range(len(c)):
  grid[ c[i][1] ][ c[i][0] ] = namestr[i]

#printGrid(grid)

countpounds = 0
for row in range(len(grid)):
  for col in range(len(grid[row])):
    if grid[row][col] in namestr:
      continue
    l = [0] * len(c)
    for i in range(len(c)):
      if (c[i][1] == row and c[i][0] == col):
        d = 0  # doesn't matter
      else:
        d = dist(c[i][1],c[i][0],row,col)
      l[i] = d

    if (sum(l) < 10000):
      grid[row][col] = '#'
      countpounds = countpounds + 1

print(countpounds)

for row in range(len(grid)):
  for col in range(len(grid[row])):
    if grid[row][col] in namestr:
      lrow = row
      lcol = col-1    
      rrow = row
      rcol = col+1
      urow = row-1
      ucol = col
      drow = row+1
      dcol = col

      if valid(lrow,lcol,rows,cols):
        if grid[lrow][lcol] == "#":
          countpounds = countpounds + 1
          continue

      if valid(rrow,rcol,rows,cols):
        if grid[rrow][rcol] == "#":
          countpounds = countpounds + 1
          continue

      if valid(urow,ucol,rows,cols):
        if grid[urow][ucol] == "#":
          countpounds = countpounds + 1
          continue

      if valid(drow,dcol,rows,cols):
        if grid[drow][dcol] == "#":
          countpounds = countpounds + 1
          continue




print(countpounds)

#printGrid(grid)

print("done.")

#pr.disable()
#pr.print_stats()













 

    
