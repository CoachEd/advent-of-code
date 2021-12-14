# part 2


"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

s = l[0]
d = {}
for i in range(2,len(l)):
  a = l[i].split(' -> ')
  d[ a[0] ] = a[1]

sz = 7000
a = [ '.' for i in range(sz) ]
idx = 0
for c in s:
  a[idx] = c
  a[idx+1] = ''
  idx += 2
idx -= 3
for step in range(  10  ):
  #print(str(step+1))
  for i in range(0, idx, 2):
    ss = a[i]+a[i+2]
    if ss in d:
      c = d[ss]
      a[i+1] = c
      
  a1 = [ '.' for i in range(sz) ]
  idx = 0
  for e in a:
    if e == '.' or e == '':
      break
    a1[idx] = e
    a1[idx+1] = ''
    idx += 2
  idx -= 3
  
  # reduce array
  
  
  a = a1.copy()
  #print(''.join(a[0:40]))
  
  


s = ''.join(a)
s = s.replace('.','')
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

#2740 too low

end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')