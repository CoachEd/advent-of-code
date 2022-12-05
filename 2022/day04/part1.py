"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

start_secs = time.time()
print('')

# day 4 pt 1
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

#55-88,78-88
count = 0
for s in l:
  arr = s.split(',')
  arr1 = arr[0].split('-')
  arr2 = arr[1].split('-')
  x1 = int(arr1[0])
  y1 = int(arr1[1])
  x2 = int(arr2[0])
  y2 = int(arr2[1])
  if (x2 >= x1 and y2 <= y1) or (x1 >= x2 and y1 <= y2):
    count += 1
    
print(count)


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
