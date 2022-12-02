"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

start_secs = time.time()
print('')



# part 1

print()
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

shape = dict()
cvt = dict()

shape['X'] = 1
shape['Y'] = 2
shape['Z'] = 3

cvt['X'] = 'A'
cvt['Y'] = 'B'
cvt['Z'] = 'C'

score = 0
for s in l:
  outcome = 0
  c1 = s[0]
  c2 = cvt[s[2]]
  if c1 == c2:
    outcome = 3
  else:
    if ((c2 == 'A' and c1 == 'C') or
    (c2 == 'B' and c1 == 'A') or
    (c2 == 'C' and c1 == 'B')):
      outcome = 6
  score += outcome + shape[s[2]]
  
print(score)
    
  



print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
