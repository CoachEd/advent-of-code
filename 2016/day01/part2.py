import sys
import time

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append(line.strip())

# TODO
arr = l[0].replace(' ','').split(',')
facing = 90 # N-90, E-180, S-270, W-0
row = 0
col = 0
w, h = 500, 500
visited = dict()
visited['0,0'] = 0 # starting point
for d in arr:
  found = False
  r1 = row
  c1 = col
  direction = d[0]
  distance = int(d[1:])
  if direction == 'R':
    facing = facing +  90
  else:
    facing = facing - 90
  if facing < 0:
    facing = 270
  elif facing > 270:
    facing = 0
  if facing == 90:
    row = row + distance
    for y in range(r1+1, row+1):
      keystr = str(y) + ',' + str(col)
      if keystr in visited:
        print('FOUND: ' + keystr + ' blocks: ' + str(abs(y) + abs(col)) )
        found = True
        break
      visited[keystr] = 0
  elif facing == 180:
    col = col + distance
    for x in range(c1+1, col+1):
      keystr = str(row) + ',' + str(x)
      if keystr in visited:
        print('FOUND: ' + keystr + ' blocks: ' + str(abs(row) + abs(x)) )
        found = True
        break
      visited[keystr] = 0    
  elif facing == 270:
    row = row - distance
    for y in range(r1-1, row-1, -1):
      keystr = str(y) + ',' + str(col)
      if keystr in visited:
        print('FOUND: ' + keystr + ' blocks: ' + str(abs(y) + abs(col)) )
        found = True
        break
      visited[keystr] = 0    
  elif facing == 0:
    col = col - distance
    for x in range(c1-1, col-1, -1):
      keystr = str(row) + ',' + str(x)
      if keystr in visited:
        print('FOUND: ' + keystr + ' blocks: ' + str(abs(row) + abs(x)) )
        found = True
        break
      visited[keystr] = 0      
  if found:
    break

# WRONG: 6, 3


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')