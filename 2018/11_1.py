
# incorrect guesses:
# 87,18
# 19,67
# Correct: 20,68

length = 300
serialno = 5791
grid = [[0 for x in range(length)] for y in range(length)]

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
    grid[y][x] = calcpower(thex,they,serialno)

# find thex, they of 3x3 grid with largest total power
savex = -1
savey = -1
totalpower = 0
for y in range(length):
  for x in range(length):
    thex = x + 1
    they = y + 1
    temppower = 0
    foundinvald = False
    for y2 in range(y,y+3):
      for x2 in range(x,x+3):
        if validc(x2,y2,length):
          temppower = temppower + grid[y2][x2]
        else:
          foundinvald = True    
    if not foundinvald and temppower > totalpower:
      totalpower = temppower
      savex = thex
      savey = they

print(str(savex) + "," + str(savey) + "  " + str(totalpower))


#s = ''
#startp = False
#for y in range(length):
#  for x in range(length):
#    outs = str(grid[y][x])
#    if grid[y][x] >= 0:
#      outs = ' '+outs
#    s = s + outs + ' , '
#  s = s + '\n'
#print(s)



