# D14 P1
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
      
  
  
def print_matrix(m):
  s = ''
  for y in range(len(m)):
    for x in range(len(m[y])):
      s += m[y][x]
    s += '\n'
  print(s)
      

# read in input file
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
l=[None for i in range(len(lines))]
for i in range(len(lines)):
  l[i] = lines[i].strip()



# SOLUTION START - start timing
start_secs = time.time()

a = [ [ c for c in l1] for l1 in l]

tiltNorth(a)

print( calcLoad(a) )

end_secs = time.time()

print('--- ' + str(end_secs-start_secs) + ' secs ---')

# SOLUTION END - stop timing

