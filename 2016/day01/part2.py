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
for d in arr:
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
  elif facing == 180:
    col = col + distance
  elif facing == 270:
    row = row - distance
  elif facing == 0:
    col = col - distance
  
  keystr = str(row)+','+str(col)
  if keystr in visited.keys():
    print('FOUND')
    break
  visited[keystr] = keystr

print('row: ' + str(row))
print('col: ' + str(col))
print('blocks: ' + str(row + col))

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')