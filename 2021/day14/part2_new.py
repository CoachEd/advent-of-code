# part 2 new
"""
AoC
"""
import time
import sys
from copy import copy, deepcopy
d = {}

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

s = l[0]
for i in range(2,len(l)):
  a = l[i].split(' -> ')
  d[ a[0] ] = a[1]

#print(s)

steps = 4
print(s)
for step in range( steps ):
  if step == 3:
    print('before: ' + s)
  for key in d:
    if step == 3:
      print(key + '->' + d[key])
    s = s.replace(key, key[0] + d[key].lower() + key[1])
    if step == 3:
      print(s)
      print('')
  s = s.upper()
  if step == 3:
    print('after  : ' + s )
    print('step: ' + str(step+1) + s)

d = {}
for c in s:
  if not c in d:
    d[c]=0
  d[c] += 1


mx = 0
mn = sys.maxsize
for key in d:
  if d[key] > mx:
    mx = d[key]
  if d[key] < mn:
    mn = d[key]
print(str(mx-mn))

end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
