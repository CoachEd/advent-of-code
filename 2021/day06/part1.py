# part 1
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


a = l[0].split(',')
a1 = [ int(i) for i in a]

arr = [ 0 for i in range(9)]
for e in a1:
  arr[e] += 1

days = 256
part1arr = []
for d in range(days):
  newarr = [ 0 for i in range(9)]
  for i in range(9):
    fishno = i
    fishcount = arr[i]
    if fishno == 0:
      newarr[6] += fishcount
      newarr[8] += fishcount
    else:
      newarr[i-1] += fishcount
  arr = newarr.copy()
  if d == 79:
    part1arr = arr.copy()

total = 0
for f in part1arr:
  total += f
print('part1: ' + str(total))

total = 0
for f in arr:
  total += f
print('part2: ' + str(total))
      


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')