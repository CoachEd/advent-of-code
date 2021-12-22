"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

instr = []
temp = []
for s in l:
  arr = s.split()
  status = arr[0]
  temp = []
  temp.append(status)
  arr2 = arr[1].split(',')
  for s1 in arr2:
    arr3 = s1.split('=')
    arr4 = arr3[1].split('..')
    temp.append([int(arr4[0]),int(arr4[1])])
  instr.append(temp)

cubes = {}
for instruction in instr:
  x1 = instruction[1][0]
  x2 = instruction[1][1]
  y1 = instruction[2][0]
  y2 = instruction[2][1]
  z1 = instruction[3][0]
  z2 = instruction[3][1]
  if x1 < -50 or x2 > 50 or y1 < -50 or y2 > 50 or z1 < -50 or z2 > 50:
    continue  
  for x in range(x1,x2+1):
    for y in range(y1,y2+1):
      for z in range(z1,z2+1):
        cube = str(x)+','+str(y)+','+str(z)
        cubes[cube] = instruction[0]

count = 0
for c in cubes:
  if cubes[c] == 'on':
    count += 1
print(count)






print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
