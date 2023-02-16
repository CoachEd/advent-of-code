import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')


# SOLUTION
# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

s = l[0] + ','
directions = ['nw,', 'n,', 'ne,', 'sw,', 's,', 'se,']

# nw n ne sw s se
while True:
  len1 = len(s)
  (d1, d2) = ('n,', 's,')
  if d1 in s and d2 in s:
    s = s.replace(d1,'',1)
    s = s.replace(d2,'',1)

  (d1, d2) = ('nw,', 'se,')
  if d1 in s and d2 in s:
    s = s.replace(d1,'',1)
    s = s.replace(d2,'',1)

  (d1, d2) = ('ne,', 'sw,')
  if d1 in s and d2 in s:
    s = s.replace(d1,'',1)
    s = s.replace(d2,'',1)    

  len2 = len(s)
  if len1 == len2:
    break

steps = 0
d1 = {}
for d in directions:
  n = s.count(d)
  d1[d] = n


for c in d1:
  print(c + ': ' + str(d1[c]))
"""
nw,: 0
n,: 0
ne,: 256
sw,: 0
s,: 43
se,: 440
"""

# s: 43 is irrelevant
# count is...

print(d1['ne,'] + d1['se,'])


# 526  TOO LOW
# 739  TOO HIGH
# 923  TOO HIGH

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')