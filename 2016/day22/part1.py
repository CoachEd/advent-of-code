"""
AoC
"""
import time

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

  node_name = str(x)+':'+str(y)
  nodes[node_num] = [x,y,size,used,avail,pct]
  node_num += 1

#print('max_x: ' + str(max_x))
#print('max_y: ' + str(max_y))
count_nodes = 0
for i in range(node_num-1):
  node_a = nodes[i]
  if node_a[3] == 0:
    # used is 0
    continue
  for j in range(i+1,node_num):
    node_b = nodes[j]
    if node_a[3] <= node_b[4]:
      # node A used will fit on node B avail
      count_nodes += 1

# opposite direction
for i in range(node_num-1,0,-1):
  node_a = nodes[i]
  if node_a[3] == 0:
    # used is 0
    continue
  for j in range(i-1,-1,-1):
    node_b = nodes[j]
    if node_a[3] <= node_b[4]:
      # node A used will fit on node B avail
      count_nodes += 1

print(count_nodes)
# 1009  # too low
# 1043  # GOOD! (A,B) and (B,A) are distinct pairs!

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
