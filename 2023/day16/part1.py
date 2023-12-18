#D16 Part 1

import time
import sys
from copy import copy, deepcopy 

def goodp(y,x,m):
  return y >= 0 and x >= 0 and y < len(m) and x < len(m[0])
  
def print_map(m):
  s = ''
  for y in range(len(m)):
    for x in range(len(m[y])):
      s += m[y][x]
    s += '\n'
  print(s)

def move_beams(mb, beams, m):
  # mb - map of just beams ###
  # m - map of mirrors and pipes
  # beams - list of beams (y,x,'E',True)
  # for each beam...
  pass
  
  

      
# read in input file
my_file = open("inp2.txt", "r", encoding='utf-8')
lines = my_file.readlines()
l=[None for i in range(len(lines))]
for i in range(len(lines)):
  l[i] = lines[i].strip()

# SOLUTION START - start timing
start_secs = time.time()

m = [ [ c for c in line ] for line in l]
mb = [ [ '.' for c in line ] for line in l]
rows = len(m)
cols = len(m[0])
beams = [ (0,0,'E',True)] # (y,x,dir,active)


# move beams until we cant
move_beams(mb, beams, m) 


end_secs = time.time()

print('--- ' + str(end_secs-start_secs) + ' secs ---')

# SOLUTION END - stop timing