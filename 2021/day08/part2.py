# part 2

"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

def has(st, letters):
  for c in letters:
    if not c in st:
      return False
  return True
  
def rem(st, letters):
  for c in letters:
    st = st.replace(c,'')
  return st

def sortl(arr):
  a2 = []
  for e in arr:
    a = []
    for c in e:
      a.append(c)
    a.sort()
    a2.append(''.join(a))
  return a2

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

# a is in 8
# b is in 6
# c is in 8
# d is in 7
# e is in 4
# f is in 9
# g is in 7
"""

 ffff
.    d
.    g
 ....
.    d
.    g
 ....

"""


digits = [0,2,0,0,4,0,0,3,7,0]


tot = 0
for s in l:
  wires = [
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  ''
  ]
  arr = s.split('|')
  aft = arr[1].split()
  aft = sortl(aft)
  bef = arr[0].split()
  bef = sortl(bef)
  all = bef + aft
  for o in all:
    l1 = len(o)
    if l1 == 2:
      wires[1] = o
    elif l1 == 4:
      wires[4] = o
    elif l1 == 3:
      wires[7] = o
    elif l1 == 7:
      wires[8] = o

  # find 3
  for o in all:
    if len(o) == 5 and has(o, wires[7]) and not o in wires:
      wires[3] = o
      
   # find 9
  for o in all:
    if len(o) == 6 and has(o, wires[3]) and not o in wires:
      wires[9] = o
  
  # find 5
  for o in all:
    if len(o) == 5 and has(wires[9],o) and not o in wires:
      wires[5] = o
      
  # find 6
  for o in all:
    if len(o) == 6 and has(o,wires[5]) and  not o in wires:
      wires[6] = o
      
  # find 0
  for o in all:
    if len(o) == 6 and has(wires[8], o) and  not o in wires:
      wires[0] = o

  # find 2
  for o in all:
    if len(o) == 5 and not o in wires and  not o in wires:
      wires[2] = o
      break

  #print(wires)
  
  s1 = ''
  for o in aft:
    s1 += str(wires.index(o))

  tot += int(s1)
  
print(tot)


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')