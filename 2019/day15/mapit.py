import sys
import time
import random

start_secs = time.time()

def BFS(board, start):
  queue = list()
  queue.append(start)
  visited = set()

  # this keeps track of where did we get to each vertex from
  # so that after we find the exit we can get back
  parents = dict()
  parents[start] = None

  while queue:
    v = queue[0]
    if board[v[0]][v[1]] == 'E':
      break
    queue = queue[1:]   # this is inefficient, an actual queue should be used 
    visited.add(v)
    for u in neighbors(board, v):
      if u not in visited:
        parents[u] = v
        queue.append(u)

  # we found the exit, now we have to go through the parents 
  # up to the start vertex to return the path
  path = list()
  while v != None:
    path.append(v)
    v = parents[v]

  # the path is in the reversed order so we reverse it 
  path.reverse()
  return path

def neighbors(board, v):
  diff = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  retval = list()
  for d in diff:
    newr = d[0] + v[0]
    newc = d[1] + v[1]
    if newr < 0 or newr >= len(board) or newc < 0 or newc >= len(board[0]):
      continue
    if board[newr][newc] == 'X': # valid path
      continue
    retval.append((newr, newc))
  return retval

s = """          # ### ### ######### # ####### ### ### #
         #.#...#...#.........#.#.......#...#...#.#
         #.#.#.#.#.#.###.###.#.#.#.###.#.#.#.#.#.#
         #...#...#...#.#.#...#...#...#...#...#.#.#
         #.## ########.#.#.#########.#########.#.#
         #...#.....#...#.#.........#.#.......#...#
          ##.#.###.###.#.#########.#.#######.###.#
         #.....#.#.....#.#.....#...#.#...#.....#.#
         #.#####.#.#####.#.###.#.###.#.#.#.#####.#
         #.#...#...#.....#.#.#.#.#...#.#.#...#...#
          ##.#.#####.#####.#.#.#.#.###.#.###.#.##
         #...#.#.....#.....#...#.#.#...#...#.....#
         #.###.#.#####.#.###.###.#.#.#####.#.####
         #...#.#...#...#.#.....#.#.#.#...#.#.#...#
         #.#.#.#.#.#####.#####.#.#.#.###.#.###.#.#
         #.#.#.#.#.....#...#...#.#.#.#...#.....#.#
         #.#.#.#######.#.#.#.###.#.#.#.#########.#
         #.#.#.........#.#.#.#.....#.#.#...#.....#
          ##.###########.#.###.#####.#.#.#.#.####
         #...#...........#.....#...#.#...#.#.....#
         #.############## ######.#.#.#.###.#####.#
         #.......#.......#...#S..#...#.# #.....#.#
         #.#####.#.#####.#.#.#########.#  ####.#.#
         #...#...#.....#...#.......#...#     #...#
          ##.#.#.#####.###########.#.##       ###
         #...#.#.#.....#.......#...#.#
         #.###.#.#.#####.#####.#.###.#
         #.#...#.#...#.#.....#.#.#...#
          ##.###.###.#.#.###.#.#.#.##         ###
         #...#...#.#.#.#...#.#.#...#         #...#
         #.###.###.#.#.###.#.##########  #.###.#.#
         #.#.#.#...#.#.#...#...........# #.....#.#
         #.#.#.#.#.#.#.#.#####.#####.#.###.#####.#
         #.#.#...#.#.#...#...#...#...#...#.....#.#
         #.#.#####.#.#####.#.###.#.#####.###.###.#
         #.#.#.....#.#.....#.#...#.#...#.#@..#...#
         #.#.#.#####.#.#####.#####.#.#.#.#####.#.#
         #.#.....#...#.#.#...#...#...#.#.....#.#.#
         #.#######.###.#.#.###.#.#####.#####.#.#.#
         #.............#.......#.......#.......#.#
          ############# ####### ####### ####### #
"""

"""
arr = s.split('\n')[:-1]
board = []
for row in arr:
  temparr = []
  for c in row:
    temparr.append(c)
  board.append(temparr)


total = 0
found1 = False
found2 = False
ry = -1
rx = -1
ey = -1
ex = -1
for y in range(0,len(board)):
  for x in range(0,len(board[y])):
    if board[y][x] == 'S':
      print('robot y,x: ' + str(y) + ',' + str(x) )
      ry = y
      rx = x
    elif board[y][x] == '@':
      print('oxygen y,x: ' + str(y) + ',' + str(x) )
      ey = y
      ex = x
    elif board[y][x] == ' ':
      board[y][x] = '#'
      pass


board[ey][ex] = 'E' # end goal
board[ry][rx] = 'R' # robot start
"""

s = """E X X O O
X X X X X
X X X O X
X X X X R
X X X X X
"""

"""
E X X O O
X X X X X
X X X O X
X X X X R
X X X X X
"""

board = s.split('\n')[:-1]


print( BFS( board, (4,3) ) )




end_secs = time.time()
print('\nelapsed time: ' + str(end_secs - start_secs) + ' seconds')