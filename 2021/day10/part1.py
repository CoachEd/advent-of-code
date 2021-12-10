# Part 1
"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

def hasl(s):
  if '(' in s or '[' in s or '{' in s or '<' in s:
    return True
  return False

def hasr(s):
  if ')' in s or ']' in s or '}' in s or '>' in s:
    return True
  return False
  
def getr(s):
  for c in s:
    if c in ')}]>':
      return c
  return ''

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

"""
If a chunk opens with (, it must close with ).
If a chunk opens with [, it must close with ].
If a chunk opens with {, it must close with }.
If a chunk opens with <, it must close with >.
"""

arr = []
for s in l:
  while True:
    len1 = len(s)
    s = s.replace('()','')
    s = s.replace('[]','')
    s = s.replace('{}','')
    s = s.replace('<>','')
    len2 = len(s)
    if len1 == len2:
      arr.append(s)
      break
    
result = ''

score = {
  ")": 3,
  "]": 57,
  "}": 1197,
  ">": 25137
}

points = 0
for s in arr:
  c = getr(s)
  if c != '':
    points += score[c]
  
print(points)
    
    



print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')