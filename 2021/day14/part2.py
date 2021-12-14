# part 2


"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

def printll(p):
  s = ''
  while p != None:
    s += p.dataval
    p = p.nextval
  print(s)

class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

s = l[0]
d = {}
for i in range(2,len(l)):
  a = l[i].split(' -> ')
  d[ a[0] ] = a[1]


# add s to linked list
list1 = SLinkedList()
list1.headval = Node(s[0])
p = list1.headval
for i in range(1,len(s)):
  e = Node(s[i])
  p.nextval = e
  p = p.nextval

for i in range(10):
  p = list1.headval
  while p != None and p.nextval != None:
    c1 = p.dataval
    c2 = p.nextval.dataval
    key = c1 + c2
    if key in d:
      insrt = d[key]
      e = Node(insrt)
      e.nextval = p.nextval
      p.nextval = e
      p = p.nextval
    p = p.nextval
  #printll(list1.headval)  


p = list1.headval
d = {}
while p != None:
  c = p.dataval
  if not c in d:
    d[c]=0
  d[c] += 1
  p = p.nextval

mx = 0
mn = sys.maxsize
for key in d:
  if d[key] > mx:
    mx = d[key]
  if d[key] < mn:
    mn = d[key]
print(str(mx-mn))

#2740 too low


end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')