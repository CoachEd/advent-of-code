"""
AoC
"""
import time
import sys
from copy import copy, deepcopy
import math

def print_m(m):
  s = ''
  for r in m:
    for c in r:
      s += c
    s += '\n'
  print(s)
  
  
start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp_sample.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

alg = l[0]
del l[0]
del l[0]

rmult = 5
cmult = 5
num_rows = len(l) * rmult
num_cols = len(l[0]) * cmult
m = [ [ '.' for r in range(num_rows) ] for c in range(num_cols) ]
midy = math.floor(num_rows / 2) - math.floor(len(l)/2)
midx = math.floor(num_cols / 2) - math.floor(len(l[0])/2)

y = midy
for r in l:
  x = midx
  for c in r:
    m[y][x] = c
    x += 1
  y += 1

print_m(m)




print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
