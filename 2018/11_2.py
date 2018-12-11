import numpy as np

# incorrect guesses:
# 87,18
# 19,67
# Correct: 20,68

# TO SLOW. DOES NOT SCALE!!!
length = 300
serialno = 5791
grid = np.zeros(shape=(length,length))

# validate coords
def validc(x,y,l):
  return (x >= 0 and y >=0 and x < l and y < l)

def calcpower(thex,they,serialno):
  rackid = thex + 10
  level = rackid * they
  level = level + serialno
  level = level * rackid
  levelstr = str(level)
  tempnum = 0
  if len(levelstr) < 3:
    tempnum = 0
  else:
    tempnum = int(levelstr[-3])
  level = tempnum
  level = level - 5
  return level

# calculate power
for y in range(length):
  for x in range(length):
    thex = x + 1
    they = y + 1
    grid[y,x] = calcpower(thex,they,serialno)

# find thex, they of 3x3 grid with largest total power
savex = -1
savey = -1
totalpower = 0
savesz = -1
for y in range(length):
  for x in range(length):
    thex = x + 1
    they = y + 1

    sz1 = length - x
    sz2 = length - y
    maxsz = 1
    if sz1 < sz2:
      maxsz = sz1 + 1
    else:
      maxsz = sz2

    for sz in range(1,maxsz):
      temppower = 0
      foundinvald = False

      if validc(x+sz-1,y+sz-1,length):
        temppower = np.sum(grid[y:y+sz,x:x+sz])
        if temppower > totalpower:
          totalpower = temppower
          savex = thex
          savey = they
          savesz = sz

print(str(savex) + ',' + str(savey) + ',' + str(savesz) + '   ' + str(totalpower))


#s = ''
#startp = False
#for y in range(length):
#  for x in range(length):
#    outs = str(grid[y,x])
#    if grid[y,x] >= 0:
#      outs = ' '+outs
#    s = s + outs + ' , '
#  s = s + '\n'
#print(s)



