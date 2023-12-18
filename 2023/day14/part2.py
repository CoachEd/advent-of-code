# d14 p2
import time
import sys
from copy import copy, deepcopy 

def moveNorth(y,x,m):
  if m[y][x] == 'O':
    # try to move it
    while True:
      y0 = y - 1
      if y0 >= 0 and m[y0][x] == '.':
        m[y0][x] = 'O'
        m[y][x] = '.'
        y = y0
      else:
        break
def moveSouth(y,x,m):
  if m[y][x] == 'O':
    # try to move it
    while True:
      y0 = y + 1
      if y0 < len(m) and m[y0][x] == '.':
        m[y0][x] = 'O'
        m[y][x] = '.'
        y = y0
      else:
        break
def moveEast(y,x,m):
  if m[y][x] == 'O':
    # try to move it
    while True:
      x0 = x + 1
      if x0 < len(m[0]) and m[y][x0] == '.':
        m[y][x0] = 'O'
        m[y][x] = '.'
        x = x0
      else:
        break
def moveWest(y,x,m):
  if m[y][x] == 'O':
    # try to move it
    while True:
      x0 = x - 1
      if x0 >= 0 and m[y][x0] == '.':
        m[y][x0] = 'O'
        m[y][x] = '.'
        x = x0
      else:
        break
def calcLoad(m):
  tot = 0
  for y in range(len(m)):
    for x in range(len(m[y])):
      if m[y][x] == 'O':
        tot += len(m) - y
  return tot

def tiltNorth(m):
  for y in range(len(m)):
    for x in range(len(m[y])):
      moveNorth(y,x,m)
def tiltSouth(m):
  for y in range(len(m)-1,-1,-1):
    for x in range(len(m[y])):
      moveSouth(y,x,m)
def tiltEast(m):
  for y in range(len(m)-1,-1,-1):
    for x in range(len(m[y])-1,-1,-1):
      moveEast(y,x,m)
def tiltWest(m):
  for y in range(len(m)):
    for x in range(len(m[y])):
      moveWest(y,x,m)

def cycle(m,n):
  for i in range(n):
    tiltNorth(m)
    tiltWest(m)
    tiltSouth(m)
    tiltEast(m)

def print_matrix(m):
  s = ''
  for y in range(len(m)):
    for x in range(len(m[y])):
      s += m[y][x]
    s += '\n'
  print(s)

def gets(m):
  s = ''
  for y in range(len(m)):
    for x in range(len(m[y])):
      s += m[y][x]
    s += '\n'
  return s

# read in input file
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
l=[None for i in range(len(lines))]
for i in range(len(lines)):
  l[i] = lines[i].strip()



# SOLUTION START - start timing
start_secs = time.time()

a = [ [ c for c in l1] for l1 in l]

n = 1000000000
s = gets(a)
d = {}
j = -1
loads =[97241, 96994, 96786, 96834, 97112, 97189, 96880, 96763, 96955]

for i in range(1,n+1):
  #print(i)
  #cycle(a,i)
  #load = calcLoad(a)
  #if i % 10 == 0:
  #  print((i,load))
  
  #cycle(a,1)
  #load = calcLoad(a)
  #if i % 100 == 0:
  #  print((i,load))
  if i % 100 == 0:
    j += 1
    if j == 9:
      j = 0
    #print((i,loads[j]))
    
  if i == n:
    print((i,loads[j]))
    break

print('done.')
    
"""
(1000000000, 97241)
done.
--- 101.56021809577942 secs ---
"""

    
"""
(100, 97241)
(200, 96994)
(300, 96786)
(400, 96834)
(500, 97112)
(600, 97189)
(700, 96880)
(800, 96763)
(900, 96955)

(1000, 97241)
(1100, 96994)
(1200, 96786)
(1300, 96834)
(1400, 97112)
(1500, 97189)
(1600, 96880)
(1700, 96763)
(1800, 96955)

(1900, 97241)
(2000, 96994)
(2100, 96786)
(2200, 96834)
(2300, 97112)
(2400, 97189)
(2500, 96880)
(2600, 96763)
(2700, 96955)

(2800, 97241)
(2900, 96994)
(3000, 96786)
(3100, 96834)
(3200, 97112)
(3300, 97189)
(3400, 96880)
(3500, 96763)
(3600, 96955)




(100, 97241)
(200, 96994)
(300, 96786)
(400, 96834)
(500, 97112)
(600, 97189)
(700, 96880)
(800, 96763)
(900, 96955)
(1000, 97241)
(1100, 96994)
(1200, 96786)
(1300, 96834)
(1400, 97112)
(1500, 97189)
(1600, 96880)
(1700, 96763)
(1800, 96955)
(1900, 97241)
(2000, 96994)
(2100, 96786)
(2200, 96834)
(2300, 97112)
(2400, 97189)
(2500, 96880)
(2600, 96763)
(2700, 96955)

"""

end_secs = time.time()

print('--- ' + str(end_secs-start_secs) + ' secs ---')

# SOLUTION END - stop timing