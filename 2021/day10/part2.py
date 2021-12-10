# part 2
"""
AoC
"""
import time
import sys
from copy import copy, deepcopy
import math

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

sc = {
  ")": 1,
  "]": 2,
  "}": 3,
  ">": 4
}

rv = {
  "(": ")",
  "[": "]",
  "{": "}",
  "<": ">"
}

inc = []
idx = -1
for s in arr:
  idx += 1
  c = getr(s)
  if c == '':
    inc.append(s)

total = 0
scores = []
for s in inc:
  s1 = ''
  score = 0
  for i in range(len(s)-1,-1,-1):
    s1 += rv[s[i]]
  for c in s1:
    score *= 5
    score += sc[c]
  scores.append(score)

scores.sort()
idx = math.trunc(len(scores)/2)
print(scores[idx])
    
    
    
"""
Did you know that autocomplete tools also have contests? It's true! The score is determined by considering the completion string character-by-character. Start with a total score of 0. Then, for each character, multiply the total score by 5 and then increase the total score by the point value given for the character in the following table:

): 1 point.
]: 2 points.
}: 3 points.
>: 4 points.
"""
    
    

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')