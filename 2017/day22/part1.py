import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

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
dsize = len(direction)
origin_y = height // 2
origin_x = width // 2
facing = 0 # up
iterations = 10000
infections = 0
for t in range(iterations):
  if a[origin_y][origin_x] == '#':
    turn_right()
    a[origin_y][origin_x] = '.'
  else:
    turn_left()
    a[origin_y][origin_x] = '#'
    infections += 1
  move()
  #print_map(a)
  #print()

print(infections)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')