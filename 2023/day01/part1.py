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
  line = line.strip()
  for c in 'abcdefghijklmnopqrstuvwxyz':
    line = line.replace(c,'')
  l.append(line)
#print(l)
# 54573 too low
tot = 0
for s in l:
  tot += int(s[0]+s[-1])
print(tot)



print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')