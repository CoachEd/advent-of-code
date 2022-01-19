"""
AoC
"""
import time
import copy

def find_xy(x,y,x2,y2,seen,arr,steps,nodes):
  nodes = copy.deepcopy(nodes)
  arr = copy.deepcopy(arr)
  # [x,y,size,used,avail,pct]
  key = str(x)+':'+str(y)
  node1 = nodes[key]
  size = node1[2]
  used = node1[3]
  if used != 0:
    print('error-must start from 000 used: ' + (x,y))
    return

  (tx,ty) = (x,y-0)
  (bx,by) = (x,y+1)
  (rx,ry) = (x+1,y)
  (lx,ly) = (x-1,y)
  good_points = []
  if has_xy(tx,ty,arr):
    good_points.append((tx,ty))
  if has_xy(bx,by,arr):
    good_points.append((bx,by))
  if has_xy(rx,ry,arr):
    good_points.append((rx,ry))
  if has_xy(lx,ly,arr):
    good_points.append((lx,ly))    
  if (x,y) in seen:
    # no back-tracking
    return
  seen.append( (x,y) )
  # next to the destination?
  if (x2,y2) in good_points:
    print(steps)
    return
  if len(good_points) > 0:
    steps += 1

    for p in good_points:
      (x1,y1) = p
      key2 = str(x1)+':'+str(y1)
      node2 = nodes[key2]
      used2 = node2[3]
      if size >= used2:
        # switch
        # [x,y,size,used,avail,pct]
        node1[3] = node2[3]
        node2[3] = 0
        arr9 = copy.deepcopy(arr)
        find_xy(x1,y1,x2,y2,seen,arr9,steps,nodes)

def has_xy(x,y,arr):
  if x < 0 or y < 0 or x >= len(arr[0]) or y >= len(arr):
    return False
  return True

def print_mem(arr,nodes):
  # [x,y,size,used,avail,pct]
  s = ''
  for r in range(len(arr)):
    for c in range(len(arr[r])):
      e = arr[r][c]
      if e[0] != -1:
        node_name = str(c)+':'+str(r)
        node = nodes[node_name]
        mem_info = "{:03d}".format(node[3]) + '/' + "{:03d}".format(node[2]) + ' '
        s += mem_info
      else:
        s += '.'
    s += '\n'
  print(s)


start_secs = time.time()
print('')

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
nodes = {}
max_x = -1
max_y = -1
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

  node_name = str(x)+':'+str(y)
  nodes[node_name] = [x,y,size,used,avail,pct]

#print('max_x: ' + str(max_x))
#print('max_y: ' + str(max_y))
cols = max_x + 1
rows = max_y + 1

# set up arr
arr = [ [ [-1,-1] for x in range(cols) ]  for y in range(rows) ]
for k,v in nodes.items():
  # [x,y,size,used,avail,pct]
  mem_location = arr[v[1]][v[0]] # y,x
  mem_location[0] = v[3] # used
  mem_location[1] = v[2] # size




find_xy(28,34,34,0,[],arr,0,nodes)


# remove nodes that cannot move
# found none?

"""
for y in range(len(arr)):
  for x in range(len(arr[y])):
    
    # top
    x1 = x
    y1 = y-1
    key1 = str(x1) +':'+str(y1)
    key = str(x) +':'+str(y)
    can_move = False
    if has_xy(x1,y1,arr) and nodes[key1][2] >= nodes[key][3]:
      continue

    # bottom
    x1 = x
    y1 = y+1
    key1 = str(x1) +':'+str(y1)
    key = str(x) +':'+str(y)
    can_move = False
    if has_xy(x1,y1,arr) and nodes[key1][2] >= nodes[key][3]:
      continue    
    
    # right
    x1 = x+1
    y1 = y
    key1 = str(x1) +':'+str(y1)
    key = str(x) +':'+str(y)
    can_move = False
    if has_xy(x1,y1,arr) and nodes[key1][2] >= nodes[key][3]:
      continue  

    # left
    x1 = x-1
    y1 = y
    key1 = str(x1) +':'+str(y1)
    key = str(x) +':'+str(y)
    can_move = False
    if has_xy(x1,y1,arr) and nodes[key1][2] >= nodes[key][3]:
      continue      

    # if we make it here, this node cannot move. remove it.
    arr[y][x] = '   .   '

print_mem(arr,nodes)
"""


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
