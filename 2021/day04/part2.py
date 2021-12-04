# part 2
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
for s in l:
  if len(s) == 0:
    b = deepcopy(board)
    arr.append(b)
    board = []
  else:
    row = s.split()
    board.append(row.copy())

a = deepcopy(arr)
bwins =[]
numwins =[]
answers = []
for n in numbers:
  winner = False
  mark(a, n)
  for i in range(0, len(a)):
    b = a[i]
    winner = isBoardWinner(b)
    if winner:
      tot = 0
      for r in b:
        for e in r:
          if e != 'X':
            tot += int(e)
      ans = tot * int(n)
      answers.append(ans)
      for i in range(0,5):
        for j in range(0,5):
          b[i][j] = ''

print(answers[-1])
print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')