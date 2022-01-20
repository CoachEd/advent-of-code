"""
AoC
"""
import time

def print_mem(arr,node_info):
  s = ''
  # [x,y,size,used,avail,pct]
  for y in range(len(arr)):
    for x in range(len(arr[y])):
      node_name = str(y)+','+str(x)
      if node_name in node_info:
        node = node_info[node_name]
        size = node[2]
        used = node[3]
        mem_info = "{:03d}".format(used) + '/' + "{:03d}".format(size) + ' '
        s += mem_info
      else:
        s += '        '
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

viable_pairs = {}
for i in range(node_num-1):
  node_a = node_list[i]
  if node_a[3] == 0:
    # used is 0
    continue
  for j in range(i+1,node_num):
    node_b = node_list[j]
    if node_a[3] <= node_b[4]:
      # node A used will fit on node B avail
      # [x,y,size,used,avail,pct]
      node_a_name = str(node_a[1])+','+str(node_a[0])
      node_b_name = str(node_b[1])+','+str(node_b[0])
      if not node_a_name in viable_pairs:
        viable_pairs[node_a_name] = []
      viable_pairs[node_a_name].append(node_b_name)

# opposite direction
for i in range(node_num-1,0,-1):
  node_a = node_list[i]
  if node_a[3] == 0:
    # used is 0
    continue
  for j in range(i-1,-1,-1):
    node_b = node_list[j]
    if node_a[3] <= node_b[4]:
      # node A used will fit on node B avail
      # [x,y,size,used,avail,pct]
      node_a_name = str(node_a[1])+','+str(node_a[0])
      node_b_name = str(node_b[1])+','+str(node_b[0])
      if not node_a_name in viable_pairs:
        viable_pairs[node_a_name] = []
      viable_pairs[node_a_name].append(node_b_name)

arr = [ [ '       ' for x in range(cols) ] for y in range(rows) ]
print_mem(arr,node_info)
#print()
#print(viable_pairs)
#print(len(viable_pairs))


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
