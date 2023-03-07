import time
import sys
from LinkedList import LinkedList
from copy import copy, deepcopy
start_secs = time.time()
print('')

def setPos():
  global steps
  global pos
  global nodes

  num_nodes = len(nodes)

  if num_nodes == 1:
    pos = 1
  else:
    rem = steps % num_nodes
    new_pos = pos + rem + 1
    if new_pos < num_nodes:
      pos = new_pos
    else:
      pos = new_pos - num_nodes

steps = 359 # real
#steps = 3 # sample

ll = LinkedList()
node = ll.insertAfter(ll.head, 0)

# part1
#insertions = 2017
#find_num = 2017

# part2
insertions = 50000000
find_num = 0

#insertions = 10
count = 0
for i in range(1, insertions + 1):
  p = node
  for j in range(steps):
    p = p.next
  node = ll.insertAfter(p, i)
  count += 1
  if count % 1000000 == 0:
    print(count)
  
  #ll.printLL()
  #print()

curr = ll.head
while curr.data != find_num:
  curr = curr.next

curr = curr.next
print()
print(curr.data)

# 39479736
# wow, took 2865 secs !




print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')