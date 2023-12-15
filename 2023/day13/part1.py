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
        (n,s1,s2) = folds[y][x]
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

    #print((i,s1,s2))
    shaved_from_left = 0
    if s1len < s2len:
      s2 = s2[0:s1len]
      s1 = s1[::-1]
    elif s2len < s1len:
      shaved_from_left = s1len-s2len
      s1 = s1[::-1]
      s1 = s1[0:s2len]

    s1len = len(s1)
    s2len = len(s2)

    #print((i,s1,s2))
    #print()
    n = 0
    for k in range(len(s1)):
      if s1[k] == s2[k]:
        n += 1
    if n == len(s1):
      n += shaved_from_left
      d[i] = (n,s1,s2)

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
fname = 'inp.txt'
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
#sys.exit()

tot = 0
for m in v:

  # check vertical
  (pos1,len1) = findBiggestFold(m)
  (pos2,len2) = findBiggestFold( rotate_matrix(m) )
  #print((pos1,len1,'  ', pos2,len2))

  if len1 > len2:
    tot += len1
  else:
    tot += 100 * len2

print()

print(tot)
end_secs = time.time()

print('--- ' + str(end_secs-start_secs) + ' secs ---')

# SOLUTION END - stop timing

# 18180 TOO LOW
# 30085 TOO LOW
# 55983 TOO HIGH