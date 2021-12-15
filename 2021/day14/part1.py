# part 1


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
steps = 10
for step in range(  steps ):
  s1 = []
  for c in s:
    s1 += ([c] + [''])
  
  for i in range(0,len(s1)-3,2):
    ss = s1[i] + s1[i+2]
    if ss in d:
      c = d[ss]
      s1[i+1] = c
  s = '%s' % ''.join(s1)
  #print('step ' + str(step+1)+': ' + str(len(s)))
  #print(s)

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

print('')
print(s)
print('')    
print(str(mx-mn))

end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
