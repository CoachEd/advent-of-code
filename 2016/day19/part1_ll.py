"""
AoC
"""
import time
import sys

# A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
    return newNode
  
  # print method for the linked list
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next
      if current == self.head:
        break
    print()

# main
#num_elves = 3014603  # does not scale well!
num_elves = 5 # test data
print('creating linked list...')
ll = LinkedList()
elf_num = 1
for i in range(num_elves):
  n = ll.insert([elf_num,1])
  if i % 1000 == 0:
    print(i)
  elf_num += 1
n.next = ll.head

print('playing...')
curr = ll.head
while True:
  arr = curr.data
  if arr[1] == num_elves:
    print('Elf ' + str(arr[0]) + ' wins!')
    break
  next_elf = curr.next
  arr[1] += next_elf.data[1]
  curr.next = next_elf.next
  curr = curr.next

start_secs = time.time()
print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
