# template.py
import time
import sys
from copy import copy, deepcopy 


### PUT BLANK LINE AT END OF INPUT FILE !!''

def rotate_matrix( m ):
  return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

def findBiggestFold(m):
  #print('findBiggestFold...')

  # TODO..
  folds =[]
  for y in range(len(m)):
    # for every row, get its fold points (i,l), pos and l chars left (including position) and l chars right of position
    folds.append(getFolds(''.join(m[y])))

  # for each possible fold point
  maxi = -1
  maxl = -1
  for x in range(len(m[0])):
    allIn = True
    for y in range(len(folds)):
      if not x in folds[y]:
        # can't consider it unless all rows have x
        allIn = False
        break
    if allIn:
      for y in range(len(folds)):
        (n,s) = folds[y][x]
        if n > maxl:
          maxl = n
          maxi = x
  return ((maxi,maxl)) # maxi pos, maxl chars to left (including maxi) and right (excluding maxi)

def getFolds(s):
  d = {} # index , (length on either side of line, s)
  for i in range(1,len(s)):
    s1 = s[0:i]
    s2 = s[i:]
    s1len = len(s1)
    s2len = len(s2)

    if s1len < s2len:
      s2 = s2[0:s1len]
      s1 = s1[::-1]
    elif s2len < s1len:
      s1 = s1[::-1]
      s1 = s1[0:s2len]
    
    s1len = len(s1)
    s2len = len(s2)
    if s1 == s2:
      d[i-1] = (len(s1),s1+s2)

  return d
    
def printOneMatrix(v,i):
  #print('printOneMatrix')
  m = v[i]
  s = ''
  for y in range(len(m)):
    for x in range(len(m[y])):
      s += m[y][x]
    s += '\n'
  print(s)

# read in input file
fname = 'inp2.txt'
with open(fname, 'r') as file:
  data = file.read()
lines = data.split('\n')
l=[None for i in range(len(lines))]
for i in range(len(lines)):
  l[i] = lines[i].strip()

# SOLUTION START - start timing
start_secs = time.time()
v = []
m = []
for y in range(len(l)):
  if len(l[y]) == 0:
    v.append(m)
    m =[]
    continue
  row = []
  for x in range(len(l[y])):
    row.append(l[y][x])
  m.append(row)

# MAIN
#printOneMatrix(v,0)

#print(  getFolds('#####..########')  )

tot = 0
for m in v:
  (pos,len1) = findBiggestFold(m)
  if pos != -1:
    tot += len1 + 1
  else:
    # not found, try rotating
    m2 = rotate_matrix(m) # cclockwise
    (pos,len1) = findBiggestFold(m2)
    tot += 100 * (len1+1)

print()

print(tot)


 

end_secs = time.time()

print('--- ' + str(end_secs-start_secs) + ' secs ---')

# SOLUTION END - stop timing