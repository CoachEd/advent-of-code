import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

def getIdx(arr, i):
  # keywords: circular list, circular array, backward, forward, reverse, steps
  # arr is a list, i is the start index, steps forward or backward (+/-)
  # if positive, insert after
  # if negative, insert before
  steps = arr[i]
  newIndex = (i + steps) % len(arr)
  if newIndex < 0:
    newIndex = len(arr) + newIndex
  return newIndex

def moveOne(arr,i):
  i2 = arr[i].index('_')  
  n = int(arr[i][0:i2]) # n value

  arr[i] = n
  to_i = getIdx(arr, i)
  arr[i] = 'ORIG'

  if n == 0:
    # do not move
    arr[i] = n
    return

  if to_i == i:
    # landed on same spot
    arr[i] = n
    return

  if n > 0:
    # insert after
    if to_i == len(arr)-1:
      # if destination is last element, just append
      arr.append(n)
    else:
      to_i += 1
      arr.insert(to_i,n)
    arr.pop(arr.index('ORIG'))
    return

  if n < 0:
    # insert before
    arr.insert(to_i, n)
    arr.pop(arr.index('ORIG'))
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
  if j in indexes:
    total += arr[i]
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
# 27130 incorrect

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')