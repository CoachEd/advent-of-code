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
  return newIndex

def moveOne(arr,i):
  n = arr[i]
  if n == 0:
    # do not move
    arr[i] = str(n)
    return arr

  to_i = getIdx(arr, i)
  if to_i == i:
    # landed on the same spot, don't move
    arr[i] = n
    return arr

  if n > 0:
    # moving to the right, insert after
    arr[i] = ' '
    to_i += 1
    if to_i >= len(arr):
      arr.append(str(n))
    else:
      arr.insert(to_i,str(n))
    arr.remove(' ')
  else:
    # moving to the left, insert before
    arr[i] = ' '
    if to_i == 0:
      # move to end
      arr.append(str(n))
    else:
      arr.insert(to_i,str(n))
    arr.remove(' ')

  return arr

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

arr = [ int(x) for x in l]

i = 0
while i < len(arr):
  n = arr[i]
  if not(type(n) == int or type(n) == float):
    i += 1
    continue
  arr = moveOne(arr,i)
  i = 0

#print(arr)

indexes = [1000, 2000, 3000]
done = False
i = arr.index('0')
j = 0

total = 0
seen = 0
while True:
  i += 1
  j += 1
  if i >= len(arr):
    i = 0
  if j in indexes:
    total += int(arr[i])
    seen += 1
    if seen == 3:
      break

print(total)
# 3898 too low
# 2785 too low
# 19808 too low



print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')