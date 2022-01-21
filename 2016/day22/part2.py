"""
AoC
"""
import time
import copy

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

print_mem(arr)

count = 0
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
        if used <= avail and is_adjacent(n1_y,n1_x,n2_y,n2_x):
          print('viable pair: ' + str((n1_y,n1_x)) + ' -> ' + str((n2_y,n2_x)))
          count += 1

print(count)
"""
start_y = 34
start_x = 28
viable_pairs = get_viable_pairs(y,x,node_list)
for k,v in viable_pairs.items():
  print(k + ': ' + str(v))
print()
print(len(viable_pairs))
"""

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
