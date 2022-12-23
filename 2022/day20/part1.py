import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

def getIdx(arr, i, steps):
  # keywords: circular list, circular array, backward, forward, reverse, steps
  # arr is a list, i is the start index, steps forward or backward (+/-)
  newIndex = (i + steps) % len(arr)
  if newIndex < 0:
    newIndex = len(arr) + newIndex
  return newIndex

def moveOne(arr,i):
  n = arr[i]
  to_i = getIdx(arr, i, n)
  if n == 0:
    # do not move
    arr[i] = str(0)
    pass
  elif n > 0:
    # moving to the right, add after
    if to_i >= len(arr):
      # end of list
      arr.append(str(n))
      arr.pop(i)
    else:
      if i < to_i:
        to_i += 1
        arr.insert(to_i,str(n))
        arr.pop(i)
      else:
        if to_i < i:
          to_i += 1
        arr.insert(to_i,str(n))
        arr.pop(i+1)
  elif n < 0:
    # moving to the left, add before
    if to_i == 0:
      arr.append(str(n))
      arr.pop(i)
    else:
      if i < to_i:
        arr.insert(to_i,str(n))
        arr.pop(i)
      else:
        arr.insert(to_i,str(n))
        arr.pop(i+1)

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
  moveOne(arr,i)
  i = 0

#print(arr)

indexes = [1000, 2000, 3000]
done = False
i = arr.index('0')
j = 0

total = 0
seen = 0
while not done:
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

arr = [3,1,3,4]
print(arr)
i = 0
moveOne(arr,i)
print(arr)


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')