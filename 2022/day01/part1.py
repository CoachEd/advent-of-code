"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

start_secs = time.time()
print('')

l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

n = 0
l2 = []
for e in l:
  if len(e) == 0:
    l2.append(n)
    n = 0
  else:
    n += int(e)
l2.append(n)

l2.sort()

print('part 1:')
print(l2[-1])
print()

mx = l2[-1] + l2[-2]+ l2[-3]
print('part 2:')
print(mx)
print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
