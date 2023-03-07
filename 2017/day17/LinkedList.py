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
  def insertAfter(self, curr, data):
    newNode = Node(data)
    if(self.head):
      # not empty
      n1 = curr.next
      curr.next = newNode
      newNode.next = n1
    else:
      # empty list
      self.head = newNode
      newNode.next = self.head
    return newNode
  
  # print method for the linked list
  # assumes circular linkedlist
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next
      if current == self.head:
        break
    print()
