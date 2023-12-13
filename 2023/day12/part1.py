import time
import sys
import re
from itertools import product
from copy import copy, deepcopy
start_secs = time.time()
print('')

"""inp3.txt
?###???????? 3,2,1
"""


# SOLUTION
def countMatches(p,a):
  n = 0
  print((p,a))
  # p pattern    '?###????????'
  # a list of gears  ['###.', '##.', '#']
  # TODO
  """
  ALGORITHM??
  """  
  return n


# read in input file
l=[]
my_file = open("inp3.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

patterns = []
sizes = []
for s in l:
  arr = s.split()
  patterns.append(arr[0])
  sizes.append([ int(c) for c in arr[1].split(',')])

gears = []
for sz in sizes:
  tempa = []
  for i in range(len(sz)):
    sep = '.'
    if i == len(sz)-1:
      sep = ''
    tempa.append(sz[i]*'#'+sep)
  gears.append(tempa)

#print(patterns)  # ['?###????????']
#print(sizes)     # [[3, 2, 1]]
#print(gears)     # [['###.', '##.', '#']]

tot_count = 0
for i in range(len(patterns)):

  count = countMatches(patterns[i],gears[i])
  tot_count += count
  print(count)

print()
print(tot_count)


 
print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')

# 6102 TOO LOW