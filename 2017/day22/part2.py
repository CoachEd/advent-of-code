import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

def change_state():
  global a, origin_y, origin_x,infections
  node = a[origin_y][origin_x]
  if node == CLEAN:
    a[origin_y][origin_x] = WEAKENED
  elif node == WEAKENED:
    a[origin_y][origin_x] = INFECTED
    infections += 1
  elif node == INFECTED:
    a[origin_y][origin_x] = FLAGGED
  elif node == FLAGGED:
    a[origin_y][origin_x] = CLEAN

def move():
  global direction, facing, origin_y, origin_x
  f = direction[facing]
  if f == 'u':
    origin_y -= 1
  elif f == 'd':
    origin_y += 1
  elif f == 'r':
    origin_x += 1
  elif f == 'l':
    origin_x -= 1

def turn_right():
  global direction, facing, dsize
  facing += 1
  if facing >= dsize:
    facing = 0

def turn_left():
  global direction, facing, dsize
  facing -= 1
  if facing < 0:
    facing = dsize - 1

def print_map(a):
  s = ''
  for r in a:
    for c in r:
      s += c + ' '
    s += '\n'
  print(s)

s = '''..#
#..
...'''.split('\n')

s = '''...#.#.####.....#.##..###
##.#.###..#.....#.##...#.
..#.##..#.#.##.#...#..###
###...##....###.#..#...#.
...#..#.........##..###..
#..#.#.#.#.#.#.#.##.####.
#...#.##...###...##..#..#
##...#.###..###...####.##
###..#.#####.##..###.#.##
#..#....#.##..####...####
...#.#......###.#..#..##.
.#.#...##.#.#####..###.#.
.....#..##..##..###....##
#.#..###.##.##.#####.##..
###..#..###.##.#..#.##.##
.#######.###....######.##
..#.#.###.##.##...###.#..
#..#.####...###..###..###
#...#..###.##..##...#.#..
........###..#.#.##..##..
.#############.#.###..###
##..#.###....#.#..#..##.#
..#.#.#####....#..#####..
.#.#..#...#...##.#..#....
##.#..#..##........#..##.'''.split('\n')

sz = len(s) // 2

width = 1000
height = 1000
y0 = height // 2 - sz
x0 = width // 2 - sz
a = [ [ '.' for x in range(width) ] for y in range(height) ]

for y in range(len(s)):
    for x in range(len(s[y])):
      a[y0+y][x0+x] = s[y][x]

direction = ['u','r','d','l']
states = ['.', 'W', '#', 'F']  # cleaned, weakened, infected, flagged
(CLEAN, WEAKENED, INFECTED, FLAGGED) = (states[0], states[1], states[2], states[3])
dsize = len(direction)
origin_y = height // 2
origin_x = width // 2
facing = 0 # up
iterations = 10000000
infections = 0
for t in range(iterations):
  node = a[origin_y][origin_x]
  if node == CLEAN:
    turn_left()
  elif node == WEAKENED:
    pass
  elif node == INFECTED:
    turn_right()
  elif node == FLAGGED:
    turn_right()
    turn_right()
  change_state()
  move()
  
  #print_map(a)
  #print()

print(infections)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')