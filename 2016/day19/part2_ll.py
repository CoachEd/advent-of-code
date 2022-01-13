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


def get_winner(num_elves):
  # main
  #num_elves = 3014603  # does not scale well!
  #num_elves = 5 # test data
  ll = LinkedList()
  elf_num = 1
  for i in range(num_elves):
    n = ll.insert([elf_num,1])
    elf_num += 1
  n.next = ll.head

  curr = ll.head
  sz = num_elves
  while True:
    arr = curr.data
    if arr[1] == num_elves:
      #print('Elf ' + str(arr[0]) + ' wins!')
      return arr[0]
      break
    move_ahead = sz // 2

    next_elf = curr
    prev = curr
    for i in range(move_ahead):
      if i < (move_ahead-1):
        prev = prev.next
      next_elf = next_elf.next
    
    #print(str(arr[0]) + ' steals from ' + str(next_elf.data[0]))
    arr[1] += next_elf.data[1]
    prev.next = next_elf.next
    curr = curr.next
    sz -= 1

start_secs = time.time()
print('')
num_elves = 3014603
#num_elves = 20

calc_winner = 1
incr = 1
elf_num = 0
for i in range(10,num_elves+1):
  elf_num = elf_num + incr
  #winner = get_winner(i)
  #print('game ' + str(i) + '  Elf ' + str(winner) + ' calc winner: ' + str(elf_num))
  if i == elf_num:
    elf_num = 0
    incr = 1
  if i // 2 == elf_num and i % 2 == 0:
    incr = 2

print(elf_num)

end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
