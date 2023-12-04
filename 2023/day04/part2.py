# Day 4 Part 1

import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')
 
# SOLUTION
def processCard(w,m,i):
  # w is winners list
  # m is mine list
  # i is card index (starting at 0)
  # n is number of winning numbers
  m2 = m.copy()
  for x in m:
    if x in w[i]:
      m2.remove(x)
  n = len(m) - len(m2)
  return n


# read in input file
l=[]
my_file = open("inp2.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

a = []
winners =[]
mine = []
for s in l:
  a1 = s.strip().split('|')
  
  s2 = a1[0].strip()
  i2 = s2.find(':')
  s2 = s2[i2+1:]
  winners.append(s2.split())
  mine.append(a1[1].strip().split())
      
score = 0
for i in range(len(mine)):
  m = mine[i]

  n = processCard(winners,m,i) # n is number of winning numbers

  g = int(2 ** (n-1))
  #print(g)
  score += g
print(score)
  

  
  

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')

