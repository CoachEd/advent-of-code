import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

def addOne(n):
  global arr
  global steps
  global pos
  if len(arr) == 1:
    arr.append(n)
    pos = 1
  else:
    rem = steps % len(arr)
    new_pos = pos + rem + 1
    if new_pos < len(arr):
      pos = new_pos
    else:
      pos = new_pos - len(arr)
    arr.insert(pos, n)

steps = 359 # real
#steps = 3 # sample
pos = 0
arr = [0]

insertions = 2017
for i in range(1, insertions + 1):
  addOne(i)

i = arr.index(2017)
if i == len(arr) - 1:
  i = 0
else:
  i += 1

print(arr[i])

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')