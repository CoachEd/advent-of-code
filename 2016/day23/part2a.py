"""
AoC
"""
import time
import sys
import math
from copy import copy, deepcopy

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

reg = {}

#reg['a'] = 7  # INPUT part 1
#reg['a'] = 12  # INPUT part 2
reg['a'] = 0
reg['b'] = 0
reg['c'] = 0
reg['d'] = 0

"""

b,d,c,a: 00007 00000 00000 00007
b,d,c,a: 00006 00000 00000 00007
b,d,c,a: 00006 00007 00000 00007
b,d,c,a: 00006 00007 00000 00000

b,d,c,a: 00006 00007 00006 00000
b,d,c,a: 00006 00007 00006 00001
b,d,c,a: 00006 00007 00005 00001
"""
def run_bunny(a1):
  b0 = a1-1
  d0 = a1
  c0 = b0 + 2
  a0 = 0
  for b in range(b0,0,-1):
    for d in range(d0,-1,-1):
      for i in range(2):
        for c in range(2):
          print('{:05d}'.format(b) + ' ' + '{:05d}'.format(d) + ' ' +'{:05d}'.format(a0) + ' ' +'{:05d}'.format(c0))
          c0 -= 1
          if c0 < 0:
            c0 = b
        a0 += 1
 


run_bunny(7)  # part 1
#run_bunny(12)  # part 2

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
