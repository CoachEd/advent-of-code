#D16 Part 1

import time
import sys
from copy import copy, deepcopy 

def goodp(y,x,m):
  return y >= 0 and x >= 0 and y < len(m) and x < len(m[0])

def count_energized(m):
  n = 0
  for y in range(len(m)):
    for x in range(len(m[y])):
      if m[y][x] == '#':
        n += 1
  return n

def print_map(m):
  s = ''
  for y in range(len(m)):
    for x in range(len(m[y])):
      s += m[y][x]
    s += '\n'
  print(s)

def get_map_str(m):
  s = ''
  for y in range(len(m)):
    for x in range(len(m[y])):
      s += m[y][x]
    s += '\n'
  return s 

def move_beams(mb, beams, m):
  # mb - map of just beams ###
  # m - map of mirrors and pipes
  # beams - list of beams (y,x,'E',True)

   allow_iterations = 10 # TODO: need to tweak higher?
   niterations = 0
   while True:
    orig_map_str = get_map_str(mb)
    active_count = 0
    new_beams = []
    for bi in range(len(beams)):
      b = beams[bi]
      (y,x,direction,active) = b
      if active:
        active_count += 1
        move_beam(beams, bi, new_beams, m, mb)

    beams = beams + new_beams
    new_map_str = get_map_str(mb)
    if orig_map_str == new_map_str:
      niterations += 1
    else:
      niterations = 0

    if (active_count == 0 and len(new_beams) == 0) or niterations > allow_iterations:
      break

def move_beam(beams, bi, new_beams, m, mb):
  (y,x,direction,active) = beams[bi]
  (y1,x1) = (y,x)

  # get next location
  if not active:
    return
  if direction == 'N':
    (y1,x1) = (y1-1,x1)
  elif direction == 'S':
    (y1,x1) = (y1+1,x1)
  elif direction == 'E':
    (y1,x1) = (y1,x1+1)
  elif direction == 'W':
    (y1,x1) = (y1,x1-1)
  else:
    print('INVALID DIRECTION: ' + direction)
    sys.exit()
  
  # Is next location a boundary?
  if not goodp(y1,x1,m):
    beams[bi] = (y,x,direction,False)  # hit boundary, no longer active
    return
  
  # process this move (tiles: . / \ | - )
  next_tile = m[y1][x1]
  next_direction = ''
  if next_tile == '.':
    mb[y1][x1] = '#'
    beams[bi] = (y1,x1,direction,active)
  elif next_tile == '/':
    if direction == 'N':
      next_direction = 'E'
    elif direction == 'S':
      next_direction = 'W'
    elif direction == 'E':
      next_direction = 'N'
    elif direction == 'W':
      next_direction = 'S'
    else:
      print('INVALID DIRECTION2: ' + direction)
      sys.exit()
    mb[y1][x1] = '#'
    beams[bi] = (y1,x1,next_direction,active)    
  elif next_tile == '\\':
    if direction == 'N':
      next_direction = 'W'
    elif direction == 'S':
      next_direction = 'E'
    elif direction == 'E':
      next_direction = 'S'
    elif direction == 'W':
      next_direction = 'N'
    else:
      print('INVALID DIRECTION3: ' + direction)
      sys.exit()
    mb[y1][x1] = '#'
    beams[bi] = (y1,x1,next_direction,active) 
  elif next_tile == '|':
    if direction == 'N' or direction =='S':
      mb[y1][x1] = '#'
      beams[bi] = (y1,x1,direction,active)
    elif direction == 'E' or direction == 'W':
      mb[y1][x1] = '#'
      beams[bi] = (y1,x1,'N',active)  # orig goes north
      new_beams.append( (y1,x1,'S',active) ) # new split goes south      
    else:
      print('INVALID DIRECTION3: ' + direction)
      sys.exit()
  elif next_tile == '-':
    if direction == 'E' or direction =='W':
      mb[y1][x1] = '#'
      beams[bi] = (y1,x1,direction,active)
    elif direction == 'N' or direction == 'S':
      mb[y1][x1] = '#'
      beams[bi] = (y1,x1,'E',active)  # orig goes east
      new_beams.append( (y1,x1,'W',active) ) # new split goes west (CAUSING A CYCLE!)
    else:
      print('INVALID DIRECTION3: ' + direction)
      sys.exit()

# read in input file
my_file = open("inp.txt", "r", encoding='utf-8')
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

# set starting point - test data
#beams = [ (0,0,'E',True)] # (y,x,dir,active)
#mb[0][0] = '#'

# starting point - real data
beams = [ (0,0,'S',True)] # (y,x,dir,active)
mb[0][0] = '#'


# move beams until we cant
move_beams(mb, beams, m) 

print_map(mb)

print( count_energized(mb) )



end_secs = time.time()

print('--- ' + str(end_secs-start_secs) + ' secs ---')

# SOLUTION END - stop timing
# 49 WRONG