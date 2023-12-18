# d13 p1
import time
import sys
from copy import copy, deepcopy


### PUT BLANK LINE AT END OF INPUT FILE !!''

def rotate_matrix( m ):
  return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

def printm(m):
  s = ''
  for y in range(len(m)):
    for x in range(len(m[y])):
      s += m[y][x]
    s += '\n'
  print(s)

def checkVert(m):

  cols = len(m[0])

  # right edge mirror?
  xstart = 0
  xend = cols - 1
  if (cols % 2) != 0:
    xstart += 1
  match = False
  pos = None
  len1 = -1
  for x in range(xstart,xend + 1, 2):
    mid = int((x+xend)/2)
    match = True
    for y in range(0,len(m)):
      s1 = m[y][x:mid+1]
      s2 = m[y][mid+1:xend+1][::-1]
      #print((s1,s2))
      if s1 != s2:
        match = False
        break
    if match:
      #print((y,x,len(s1)))
      len1 = x+len(s1)
      pos = x
      break
  if match:
    #print('right edge')
    return (len1,len1)

  # left edge mirror?
  xstart = 0
  xend = cols - 1
  if (cols % 2) != 0:
    xend -= 1
  match = False
  pos = None
  len1 = -1
  for x in range(xend,0,-2):
    mid = int((x+1)/2) # 4
    match = True
    for y in range(0,len(m)):
      s1 = m[y][0:mid]
      s2 = m[y][mid:x+1][::-1]
      if s1 != s2:
        match = False
        break
    if match:
      len1 = mid
      pos = x - mid + 1
      break
  if match:
    #print('return left edge')
    return (pos,pos)
    
  return(-1,-1)

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

tot = 0
for m in v:
  if len(m) == 0:
    continue
  
  (pv,lv) = checkVert(m)
  
  mrot = deepcopy(m)
  mrot = rotate_matrix(mrot)
  (ph,lh) = checkVert(mrot)
  
  #printm(m)
  #print(('v',pv,lv,'  h',ph,lh))
  
  if pv != -1:
    tot += pv
  elif ph != -1:
    tot += 100 * ph
  else:
    print('should not happen')
    
print(tot)
  





print()
end_secs = time.time()

print('--- ' + str(end_secs-start_secs) + ' secs ---')

# SOLUTION END - stop timing

# 18180 TOO LOW
# 30085 TOO LOW
# 55983 TOO HIGH
# 48765
# 50600

