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

arr =[]
for s in l:
  mid = int(len(s)/2)
  first = s[0:mid]
  second = s[mid:]
  for c in first:
    if second.find(c) != -1:
      arr.append(c)
      break

tot =0
for c in arr:
  #97-122 a-z
  #65-90 A-Z
  val = 0
  if c.islower():
    val = ord(c) - 96
  else:
    val = ord(c) - 38
  tot += val
print(tot)



print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
