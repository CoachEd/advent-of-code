"""
AoC
"""
import time

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

#print_mem(arr,nodes)



print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
