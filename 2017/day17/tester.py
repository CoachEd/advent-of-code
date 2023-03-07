from LinkedList import LinkedList
import random

# main
num_nodes = 5
ll = LinkedList()
for i in range(num_nodes):
  d = random.randint(0, 100) # random data
  print('inserting ' + str(d) + ' ...')
  ll.insertAfter(ll.head, d)

# testing
print('printing...')
ll.printLL()

n = ll.head.next.next
ll.insertAfter(n, -1)

print('printing...')
ll.printLL()
