"""
AoC
"""
import time
import copy
import sys

empty_y = 34
empty_x = 28
target_y = 0
target_x = 29
steps = 0

def move_node(y,x,direction,arr):
  global empty_y
  global empty_x
  global steps
  if arr[y][x][0] != 0:
    print('not 0')
    return False

  y1 = y
  x1 = x
  if direction == 'up':
    y1 -= 1
  elif direction == 'down':
    y1 += 1
  elif direction == 'right':
    x1 += 1
  elif direction == 'left':
    x1 -= 1
  if not is_valid(y1,x1):
    print('not valid')
    return False

  # can dest node data fit in y,x ?
  dest_used = arr[y1][x1][0]
  curr_avail = arr[y][x][1]
  if dest_used > curr_avail:
    # cannot fit
    print('cannot fit')
    return False

  # move it, move it
  steps += 1
  arr[y][x][0] = arr[y1][x1][0]
  arr[y][x][1] -= arr[y][x][0]
  arr[y1][x1][1] += arr[y1][x1][0]
  arr[y1][x1][0] = 0
  empty_y = y1
  empty_x = x1
  return True


def is_valid(y,x):
  global rows
  global cols
  if y < 0 or x < 0 or y >= rows or x >= cols:
    return False
  return True

def is_adjacent(y1,x1,y2,x2):
  ty = y1-1
  tx = x1
  by = y1+1
  bx = x1
  ry = y1
  rx = x1+1
  ly = y1
  lx = x1-1
  if is_valid(ty,tx) and ty == y2 and tx == x2:
    return True
  if is_valid(by,bx) and by == y2 and bx == x2:
    return True    
  if is_valid(ry,rx) and ry == y2 and rx == x2:
    return True
  if is_valid(ly,lx) and ly == y2 and lx == x2:
    return True
  return False

def print_mem(arr):
  s = ''
  for y in range(len(arr)):
    for x in range(len(arr[y])):
      arr2 = arr[y][x]
      used = arr2[0]
      size = arr2[1]
      s += "{:03d}".format(used) + '/' + "{:03d}".format(size) + ' '
    s += '\n'
  print(s)

start_secs = time.time()

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  len_line = 0
  line = line.strip()
  while len_line != len(line):
    len_line = len(line)
    line = line.replace('  ',' ')

  l.append(line)

# Filesystem              Size  Used  Avail  Use%
# /dev/grid/node-x29-y27   92T   72T    20T   78%
node_list = {}
node_info = {}
max_x = -1
max_y = -1
node_num = 0
for i in range(2,len(l)):
  arr = l[i].split(' ')
  arr2 = arr[0].split('-')
  x = int(arr2[1][1:])
  y = int(arr2[2][1:])
  if x > max_x:
    max_x = x
  if y > max_y:
    max_y = y
  
  size = arr[1]
  i = size.find('T')
  size = int(size[0:i])

  used = arr[2]
  i = used.find('T')
  used = int(used[0:i])

  avail = arr[3]
  i = avail.find('T')
  avail = int(avail[0:i])

  pct = arr[4]
  i = pct.find('%')
  pct = int(pct[0:i])  

  node_name = str(y)+','+str(x)
  node_list[node_num] = [x,y,size,used,avail,pct]
  node_info[node_name] = [x,y,size,used,avail,pct]
  node_num += 1

cols = max_x + 1
rows = max_y + 1
#print('cols: ' + str(cols)) # 35
#print('rows: ' + str(rows)) # 30

arr = [ [ '       ' for x in range(cols) ] for y in range(rows) ]
# [x,y,size,used,avail,pct]
for y in range(len(arr)):
  for x in range(len(arr[y])):
    node_name = str(y)+','+str(x)
    if node_name in node_info:
      node = node_info[node_name]
      used = node[3]
      avail = node[4]
      arr[y][x] = [used,avail]
    else:
      arr[y][x] = [-1,-1]

# count viable pairs
count_viable_pairs = 0
for y in range(len(arr)):
  for x in range(len(arr[y])):
    n1_y = y
    n1_x = x
    used =  arr[n1_y][n1_x][0]
    if used == 0:
      continue
    for y2 in range(len(arr)):
      for x2 in range(len(arr[y2])):
        n2_y = y2
        n2_x = x2
        if n1_y == n2_y and n1_x == n2_x:
          continue
        avail = arr[n2_y][n2_x][1]
        #if used <= avail and is_adjacent(n1_y,n1_x,n2_y,n2_x):
        if used <= avail:
          #print('viable pair: ' + str((n1_y,n1_x)) + ' -> ' + str((n2_y,n2_x)))
          count_viable_pairs += 1


#print(count_viable_pairs)


"""
empty_y = 34
empty_x = 28
target_y = 0
target_x = 29
"""
print_mem(arr)
print((empty_y,empty_x,steps))

# up 13
for i in range(13):
  move_node(empty_y,empty_x,'up',arr)

# left 5
for i in range(5):
  move_node(empty_y,empty_x,'left',arr)

# up 21
for i in range(21):
  move_node(empty_y,empty_x,'up',arr)

# right 5 (next to target)
for i in range(5):
  move_node(empty_y,empty_x,'right',arr)

# do si do
for i in range(28):
  move_node(empty_y,empty_x,'right',arr)
  move_node(empty_y,empty_x,'down',arr)
  move_node(empty_y,empty_x,'left',arr)
  move_node(empty_y,empty_x,'left',arr)
  move_node(empty_y,empty_x,'up',arr)

move_node(empty_y,empty_x,'right',arr) # last move

print()
print_mem(arr)
print((empty_y,empty_x,steps))

print('steps: ' + str(steps))


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
