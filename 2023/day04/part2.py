# Day 4 Part 1

import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')
 
# SOLUTION
def processCard(w,m):
  # w is winners list
  # m is mine list
  # i is card index (starting at 0)
  # n is number of winning numbers
  m2 = m.copy()
  for x in m:
    if x in w:
      m2.remove(x)
  n = len(m) - len(m2)
  return n


# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
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
card_count = [1 for i in range(len(mine)+1)]
card_count[0] = 0 # do not use 0
cards_to_process = {} # do not use 0
for i in range(1,len(card_count)):
  cards_to_process[i] = 1

while len(cards_to_process) > 0:
  for k,v in cards_to_process.items():
    # process card k
    if cards_to_process[k] == 0:
      continue

    cards_to_process[k] -= 1
    j = k - 1

    num_winners = processCard(winners[j],mine[j])
    copy_start = k + 1
    for l in range(copy_start,copy_start+num_winners):
      cards_to_process[l] += 1
      card_count[l] += 1
  c2 = cards_to_process.copy()
  for k,v in c2.items():
    if v == 0:
      del cards_to_process[k]

score = 0
for n in card_count:
  score += n
print(score)

  


"""
for i in range(len(mine)):
  m = mine[i]

  n = processCard(winners,m,i) # n is number of winning numbers
  card_num = i + 1
"""

  

  
  

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')

