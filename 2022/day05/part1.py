"""
AoC
"""
import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')


# day 5 pt 1
"""
[M]                     [N] [Z]    
[F]             [R] [Z] [C] [C]    
[C]     [V]     [L] [N] [G] [V]    
[W]     [L]     [T] [H] [V] [F] [H]
[T]     [T] [W] [F] [B] [P] [J] [L]
[D] [L] [H] [J] [C] [G] [S] [R] [M]
[L] [B] [C] [P] [S] [D] [M] [Q] [P]
[B] [N] [J] [S] [Z] [W] [F] [W] [R]
 1   2   3   4   5   6   7   8   9 
"""
a = []
a.append([])
a.append(['B','L','D','T','W','C','F','M'])
a.append(['N','B','L'])
a.append(['J','C','H','T','L','V'])
a.append(['S','P','J','W'])
a.append(['Z','S','C','F','T','L','R'])
a.append(['W','D','G','B','H','N','Z'])
a.append(['F','M','S','P','V','G','C','N'])
a.append(['W','Q','R','J','F','V','C','Z'])
a.append(['R','P','M','L','H'])

print()
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

# move 5 from 3 to 6
for s in l:
  instr = s.split(' ')
  count = int(instr[1])
  fr = int(instr[3])
  to = int(instr[5])
  for i in range(count):
    a[to].append(a[fr].pop())

s = ''
for i in range(1, len(a)):
  s += a[i][-1]
  
print(s)


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')