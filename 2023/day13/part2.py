import time
import sys
from copy import copy, deepcopy


### PUT BLANK LINE AT END OF INPUT FILE !!''

def rotate_matrix( m ):
  return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

def checkVert(om,opos,oor):
  m = deepcopy(om)
  for y in range(len(m)):
    for x in range(len(m[y])):
      orig = m[y][x]
      if m[y][x] == '.':
        m[y][x] = '#'
      else:
        m[y][x] = '.'
      (pos0,len0)=findBiggestFold( m )
      m[y][x] = orig
      
      #if pos0 != -1:
      #  print('checkvert',pos0,opos,oor)
      if pos0 != -1 and (oor == 'h' or pos0 != opos):
        #print( ('checkvert',pos0,len0) )
        return (pos0,len0)
  #print()
  #print()
  return (-1,-1)

def checkHoriz(om,opos,oor):
  m = deepcopy(om)
  m = rotate_matrix(m)
  for y in range(len(m)):
    for x in range(len(m[y])):
      #print((y,x))


      orig = m[y][x]
      if m[y][x] == '.':
        m[y][x] = '#'
      else:
        m[y][x] = '.'
      (pos0,len0)=findBiggestFold( m )
      m[y][x] = orig
      if pos0 != -1 and (oor == 'v' or pos0 != opos):
        #print( (pos0,len0) )
        #print(('return',pos0,opos,len0))
        return (pos0,len0)
  #print()
  return (-1,-1)

def findBiggestFold(om):
  #print('findBiggestFold...')
  m = deepcopy(om)
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

"""
capture part 1 vert or horiz and pos in array
try findNewVert or findNreHoriz
if orig was horiz and found vert, we are done
if orig was horiz and we found horiz, we are done if pos moved
if orig was vert and we found vert, we are done if pos moved
"""
# GET previous orientations
orientations = []
for m9 in v:
  
  # check vertical
  m = deepcopy(m9)
  (pos1,len1) = findBiggestFold(m)
  
  # check horizontal
  mr = deepcopy(m9)
  (pos2,len2) = findBiggestFold( rotate_matrix(mr) )

  #print((pos1,len1))
  #print((pos2,len2))
  #sys.exit()

  if pos1 != -1:
    orientations.append(('v',pos1,len1))
  else:
    orientations.append(('h',pos2,len2))

# GO
tot = 0
processed = 0
for i in range(len(v)):

  m = v[i]
  if len(m) == 0:
    continue

  om = deepcopy(m)

  (oor,opos,_) = orientations[i]

  (pos3,len3) = checkVert(om,opos,oor)
  (pos4,len4) = checkHoriz(om,opos,oor)
  
  #print((pos3,len3))
  #print((pos4,len4))
  #sys.exit()
  
  if oor == 'v' and  pos4 != -1:
    tot += len4 * 100
  elif oor == 'h' and pos3 != -1:
    tot += len3
  else:
    if pos3 != -1:
      tot += len3
    else:
      tot += len4 * 100
  processed += 1
  
#print(('processed: ', processed))
print()

print(tot)
end_secs = time.time()

print('--- ' + str(end_secs-start_secs) + ' secs ---')

# SOLUTION END - stop timing

# 18180 TOO LOW
# 30085 TOO LOW
# 55983 TOO HIGH
# 48765
# 50600
