import sys
import time

start_secs = time.time()
#Represents the node of list.    
class Node:    
  def __init__(self,data):    
    self.data = data    
    self.next = None    
     
class CreateList:    
  #Declaring head and tail pointer as null.    
  def __init__(self):    
    self.head = Node(None)    
    self.tail = Node(None)    
    self.head.next = self.tail    
    self.tail.next = self.head    
        
  #This function will add the new node at the end of the list.    
  def add(self,data):    
    newNode = Node(data)    
    #Checks if the list is empty.    
    if self.head.data is None:    
      #If list is empty, both head and tail would point to new node.    
      self.head = newNode    
      self.tail = newNode    
      newNode.next = self.head    
    else:    
      #tail will point to new node.    
      self.tail.next = newNode    
      #New node will become new tail.    
      self.tail = newNode    
      #Since, it is circular linked list tail will point to head.    
      self.tail.next = self.head    
     
  #Displays all the nodes in the list    
  def display(self):    
    current = self.head    
    if self.head is None:    
      print("List is empty")    
      return    
    else:    
        print("Nodes of the circular linked list: ")    
        #Prints each node by incrementing pointer.    
        print(current.data),    
        while(current.next != self.head):    
            current = current.next    
            print(current.data),    
     

def print_list(l):
    c = l.head
    s = str(c.data) + ' '
    c = c.next
    while c != l.head:
        s = s + str(c.data) + ' '
        c = c.next
    print(s)

s = '389125467'
cl = CreateList()    
for c in s:
    cl.add(int(c))   
#cl.display()  


curr = cl.head
for i in range(0,10):
    # pick up three
    new_curr = curr
    three = []

    old_curr = curr.next
    for i in range(0,3):
        new_curr = new_curr.next
        three.append(new_curr.data)
    for i in range(0,3):
        temp = old_curr
        old_curr = old_curr.next
        del temp

    new_curr = new_curr.next
    curr.next = new_curr

    cups = []
    curr1 = curr
    cups.append(curr1.data)
    curr1 = curr1.next
    max_cup = -1 * sys.maxsize
    min_cup = sys.maxsize
    while curr1 != curr:
        if curr1.data > max_cup:
            max_cup = curr1.data
        if curr1.data < min_cup:
            min_cup = curr1.data
        cups.append(curr1.data)
        curr1 = curr1.next

    # select dest cup
    dest_cup = curr.data - 1
    while dest_cup in three:
        dest_cup = dest_cup - 1
        if dest_cup < min_cup:
            dest_cup = max_cup

    # place cups
    dest = cl.head
    while dest.data != dest_cup:
        dest = dest.next
    nextn = dest.next
    cl2 = CreateList()    
    for n in three:
        cl2.add(n)
    dest.next = cl2.head
    cl2.tail.next = nextn

    print_list(cl)
    curr = curr.next
    cl.head = curr





print()
end_secs = time.time()
print(str(end_secs-start_secs))