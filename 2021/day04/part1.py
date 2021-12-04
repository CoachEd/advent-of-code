
# part 1
"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

start_secs = time.time()
print('')

def mark(arr, n):
  for b in arr:
    for r in range(0,5):
      for c in range(0,5):
        if b[r][c] == n:
          b[r][c] = 'X'

def isBoardWinner(b):
  # check rows
  for r in b:
    if  ''.join(r) == 'XXXXX':
      return True

  # check cols
  for x in range(0,5):
    s = ''
    for y in range(0,5):
      s += b[y][x]
    if s == 'XXXXX':
      return True

  return False

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

numbers = l[0].split(',')
l = l[2:]

arr = []
board = []
lineno = -1
for s in l:
  lineno += 1
  if len(s) == 0 or lineno == len(l):
    b = deepcopy(board)
    arr.append(b)
    board = []
  else:
    row = s.split()
    board.append(row.copy())

a = deepcopy(arr)
bans = []
wnum = 0
for n in numbers:
  winner = False
  mark(a, n)
  for b in a:
    winner = isBoardWinner(b)
    if winner:
      bans = deepcopy(b)
      wnum = n
      break
  if winner:
    break

tot = 0
for r in bans:
  for e in r:
    if e != 'X':
      tot += int(e)
ans = tot * int(wnum)
print(ans)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')