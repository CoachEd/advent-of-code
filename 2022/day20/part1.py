import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

def getIdx(arr, i):
  # keywords: circular list, circular array, backward, forward, reverse, steps
  # arr is a list, i is the start index, steps forward or backward (+/-)
  steps = arr[i]
  newIndex = (i + steps) % len(arr)
  if newIndex < 0:
    newIndex = len(arr) + newIndex
  if arr[i] > 0:
    newIndex += 1
    if newIndex >= len(arr):
      newIndex = 0
  return newIndex

def moveOne(arr,i):
  i2 = arr[i].index('_')  
  n = int(arr[i][0:i2])
  arr[i] = n

  if n == 0:
    # do not move
    arr[i] = n
    return

  to_i = getIdx(arr, i)

  after_i = i + 1
  if after_i >= len(arr):
    after_i = 0

  if to_i == after_i:
    # same spot, no change
    arr[i] = n
    return
  
  if to_i == 0 or to_i < i:
    arr.pop(i)
    arr.insert(to_i, n)
    return
  
  if to_i > i:
    to_i -= 1
    arr.pop(i)
    arr.insert(to_i, n)
    return
  
  return

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

arr = [ l[i] + '_' + str(i) for i in range(len(l)) ]
arr2 = arr.copy()

for s in arr2:
  i = arr.index(s)
  moveOne(arr, i)

indexes = [1000, 2000, 3000]
i = arr.index(0)
j = 0
total = 0
seen = 0
while True:
  if j == 1000 or j == 2000 or j == 3000:
    total += int(arr[i])
    seen += 1
    if seen == 3:
      break
  i += 1
  j += 1

  if i >= len(arr):
    i = 0

print()
print(total)
# 3898 too low
# 2785 too low
# 19808 too low



print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')