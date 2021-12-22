"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

start_secs = time.time()
print('')

board_len = 10
board = [ (n+1) for n in range(board_len)]

di = 0
dice = [ x for x in range(1,101) ]
def roll():
  global di
  global dice
  n = dice[di]
  di += 1
  if di >= len(dice):
    di = 0
  return n

def move_forward(p,n,pstart):
  global board_len
  global board

  curr_pos = pstart[p-1]
  end_pos = (curr_pos + n) % 10
  pstart[p-1] = end_pos
  return end_pos

def play_game(pstart,pscores):
  player = 1
  rolls = 0
  while True:
    r1 = roll()  # TODO: this should open parallel universe with roll 1
    r2 = roll()  # TODO: this should open parallel universe with roll 1
    r3 = roll()  # TODO: this should open parallel universe with roll 1
    r = r1 + r2 + r3
    rolls += 3
    spot = move_forward(player,r,pstart)
    pscores[player-1] += board[spot]
    if player == 2:
      player = 1
    else:
      player = 2  
    if pscores[0] >= 1000 or pscores[1] >= 1000:
      break
  return (pscores, rolls)

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

pstart = []
for s in l:
  arr = s.split(':')
  pstart.append(int(arr[1])-1)
pscores = [0,0]

(pscores, rolls) = play_game(pstart,pscores)

# result
if pscores[0] < pscores[1]:
  print(rolls * pscores[0])
else:
  print(rolls * pscores[1])



  





print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
