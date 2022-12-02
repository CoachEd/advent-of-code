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
symbol = dict()
outc = dict()

shape['X'] = 1
shape['Y'] = 2
shape['Z'] = 3

cvt['X'] = 'A'
cvt['Y'] = 'B'
cvt['Z'] = 'C'

symbol['A'] = '👊'
symbol['B']  = '✋'
symbol['C']  = '🤞'
outc[6] = '✅'
outc[0] = '❌'
outc[3] = '➖'

sys.stdout.write('\033c') # clear screen
score = 0
for s in l:
  outcome = 0
  c1 = s[0]
  c2 = cvt[s[2]]
  s1 = symbol[c1]
  s2 = symbol[c2]
  if c1 == c2:
    outcome = 3
  else:
    if ((c2 == 'A' and c1 == 'C') or
    (c2 == 'B' and c1 == 'A') or
    (c2 == 'C' and c1 == 'B')):
      outcome = 6      
  score += outcome + shape[s[2]]
  game = s1 + ' ' + s2 + ' ' + outc[outcome] + ':  ' + str(score)
  print(game)
  time.sleep(0.10)
  sys.stdout.write('\033c') # clear screen
  
print(score)
    
  



print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
