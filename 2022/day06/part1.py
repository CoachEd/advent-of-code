# day 6 p1 and p2

import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

markerLen = 4 # part 1
# markerLen = 14 # part 2
def isMarker(i,arr):
  global markerLen
  arr2 = arr[i:i+markerLen]
  arr2.sort()
  for j in range(len(arr2)-1):
    if (arr2[j] == arr2[j+1]):
      return False
  return True
  
# SOLUTION
# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())
s = l[0]

arr = list(s)
count = 0
for i in range(len(arr)):
  if isMarker(i, arr):
    break
  count += 1
count += markerLen
print(count)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')