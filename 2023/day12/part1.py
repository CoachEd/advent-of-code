import time
import sys
from copy import copy, deepcopy
import itertools as IT

# read in input file
my_file = open("inp2.txt", "r", encoding='utf-8')
lines = my_file.readlines()
l=[None for i in range(len(lines))]
for i in range(len(lines)):
  l[i] = lines[i].strip()

patterns = []
sizes = []
for s in l:
  arr = s.split()
  patterns.append(arr[0])
  sizes.append([ int(c) for c in arr[1].split(',')])

def isMatch(p,s):
  # p is the pattern to match:
  #                ?###????????
  # s is a potential
  #  match         .###.##..#..
  #  no match:     ###.##.....#
  # return True/False
  # TODO: See https://stackoverflow.com/questions/4697882/how-can-i-find-all-matches-to-a-regular-expression-in-python
  
  #print((p,s))
  
  return False

def arrangements(a,n):
  # arrangements of groups must always have one '.' between them at minimum
  # a is the array of int sizes: [3,2,1]
  # n is length of string
  # example for [3,2,1],12
  #             .###.##...#.
  # return array of all possible arrangements

  # get minimal pattern using sizes
  s = ''
  for i in range(len(a)):
    s = s + '#' * a[i]
    if i < len(a)-1:
      s += '.'
  plen = len(s)
  extra = n - plen
  l = []
  num_dots = s.count('.')
  extra += num_dots
  for s1 in s.split('.'):
    l.append(s1)
  
  for i in range(extra):
    l.append('.')

  
  perms = list(IT.permutations(l))
  permsu = set()
  for p in perms:
    permsu.add(''.join(p))
  return list(permsu)


# SOLUTION START - start timing
start_secs = time.time()
# TODO

tot_passed = 0
for i in range(len(patterns)):
  p = patterns[i]
  sz = sizes[i]
  arr = arrangements(sz,len(p))
  num_passed = 0
  for s in arr:
    if isMatch(p,s):
      num_passed = 0
  #print(num_passed)
  tot_passed += num_passed
  #print(i)
  
#print(tot_passed)
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
# SOLUTION END - stop timing