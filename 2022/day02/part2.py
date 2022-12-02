"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

start_secs = time.time()
print('')




print()
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

shape = dict()
cvt = dict()
lvt = dict()

shape['X'] = 1
shape['Y'] = 2
shape['Z'] = 3
shape['A'] = 1
shape['B'] = 2
shape['C'] = 3

cvt['A'] = 2
cvt['B'] = 3
cvt['C'] = 1


lvt['A'] = 3
lvt['B'] = 1
lvt['C'] = 2

  
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

score = 0
for s in l:
  c1 = s[0]
  outcome = 0
  points = lvt[c1]
  if s[2] == 'Y':
    outcome = 3
    points = shape[c1]
  elif s[2] == 'Z':
    outcome = 6
    points = cvt[c1]
  score += outcome + points
  
  
print(score)
    

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
