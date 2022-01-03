"""
AoC
"""
import time
import sys
from copy import copy, deepcopy
from numpy import rot90, array

def roll(v): return (v[0],v[2],-v[1])
def turn(v): return (-v[1],v[0],v[2])
def sequence (v):
    for cycle in range(2):
        for step in range(3):  # Yield RTTT 3 times
            v = roll(v)
            yield(v)           #    Yield R
            for i in range(3): #    Yield TTT
                v = turn(v)
                yield(v)
        v = roll(turn(roll(v)))  # Do RTR

start_secs = time.time()
print('')

# read in input file
d=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
scanner_num = 0
points = []
for line in lines:
  # --- scanner 0 ---
  s = line.strip()
  if s.startswith('---'):
    continue
  if len(s) == 0:
    d.append(points)
    points = []
    scanner_num += 1
    continue
  arr = [ int(x) for x in s.split(',')]
  points.append(arr)
d.append(points)
  
# d is an array of scanners data; each scanner's data is an array of point x,y,z
d2 = []
for n in range(len(d)):
  temparr = []
  for i in range(len(d[n])):
    point = d[n][i]
    x = set()
    p = sequence(( point[0],point[1],point[2] ))
    for i in p:
      x.add(i)
    temparr.append(x)
  d2.append(temparr)

for i in range(len(d2)):
  for j in range(i+1,len(d2)-1):
    sc1 = d2[i]
    sc2 = d2[j]
    for A in sc1:
      for B in sc2:
        if len(A.intersection(B)) > 0:
          print('scanner ' + str(i) + ',scanner ' + str(j) + '  matched')
    



print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
