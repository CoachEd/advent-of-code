import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

def get_pattern(a):
  global patterns, rules

  for i in range(len(rules)):
    r = rules[i]
    if len(r) != len(a):
      continue
    if is_match(a, r):
      return patterns[i]
  return []

def is_match(a, r):
  len1 = len(a)
  if len1 == 3:
    # no rotation
    t1 = (r[0][0], r[0][1], r[0][2], r[1][0], r[1][1], r[1][2], r[2][0], r[2][1], r[2][2])
    t2 = (a[0][0], a[0][1], a[0][2], a[1][0], a[1][1], a[1][2], a[2][0], a[2][1], a[2][2])
    if t1 == t2:
      return True
    
    # rotate a one turn
    t1 = (r[0][0], r[0][1], r[0][2], r[1][0], r[1][1], r[1][2], r[2][0], r[2][1], r[2][2])
    t2 = (a[2][0], a[1][0], a[0][0], a[2][1], a[1][1], a[0][1], a[2][2], a[1][2], a[0][2])
    if t1 == t2:
      return True

    # rotate a one turn
    t1 = (r[0][0], r[0][1], r[0][2], r[1][0], r[1][1], r[1][2], r[2][0], r[2][1], r[2][2])
    t2 = (a[2][2], a[2][1], a[2][0], a[1][2], a[1][1], a[1][0], a[0][2], a[0][1], a[0][0])
    if t1 == t2:
      return True
    
    # rotate a one turn
    t1 = (r[0][0], r[0][1], r[0][2], r[1][0], r[1][1], r[1][2], r[2][0], r[2][1], r[2][2])
    t2 = (a[0][2], a[1][2], a[2][2], a[0][1], a[1][1], a[2][1], a[0][0], a[1][0], a[2][0])
    if t1 == t2:
      return True  
    
    return False
  elif len1 == 2:
    # no rotation
    t1 = (r[0][0], r[0][1], r[1][0], r[1][1])
    t2 = (a[0][0], a[0][1], a[1][0], a[1][1])
    if t1 == t2:
      return True
    
    # rotate one turn
    t1 = (r[0][0], r[0][1], r[1][0], r[1][1])
    t2 = (a[1][0], a[0][0], a[1][1], a[0][1])
    if t1 == t2:
      return True  
    
    # rotate one turn
    t1 = (r[0][0], r[0][1], r[1][0], r[1][1])
    t2 = (a[1][1], a[1][0], a[0][1], a[0][0])
    if t1 == t2:
      return True    

    # rotate one turn
    t1 = (r[0][0], r[0][1], r[1][0], r[1][1])
    t2 = (a[0][1], a[1][1], a[0][0], a[1][0])
    if t1 == t2:
      return True    
  else:
    print('error! no match for length: ' + str(len1))

# read in input file
rules=[]
patterns=[]
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

for s in l:
  s = s.replace(' ','').replace('=>',',')
  a = s.split(',')
  rules.append(a[0].split('/'))
  patterns.append(a[1].split('/'))

# starting image
image = '.#./..#/###'.split('/')

# TEST
p = get_pattern(image)
print(p)

iterations = 5
for i in range(iterations):
  pass




print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')