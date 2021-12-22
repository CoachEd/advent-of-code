"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

start_secs = time.time()
print('')

wins = [0,0]

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

def play_game(player,dice,pstart,pscores):
  global wins
  if pscores[0] >= 21:
    wins[0] += 1
    return
  if pscores[1] >= 21:
    wins[1] += 1
    return
  
  if not -1 in dice:
    r = dice[0] + dice[1] + dice[2]
    spot = move_forward(player,r,pstart)
    pscores[player-1] += board[spot]
    if pscores[player-1] >= 21:
      wins[player-1] += 1
      return
    dice[0] = -1
    dice[1] = -1
    dice[2] = -1
    # next turn
    if player == 1:
      player = 2
    else:
      player = 1
    play_game(player,dice,pstart.copy(),pscores.copy())
  else:
    # roll 1, 2, 3
    dice1 = dice.copy()
    dice2 = dice.copy()
    dice3 = dice.copy()
    if dice[0] == -1:
      dice1[0] = 1
      dice2[0] = 2
      dice3[0] = 3
    elif dice[1] == -1:
      dice1[1] = 1
      dice2[1] = 2
      dice3[1] = 3
    elif dice[2] == -1:
      dice1[2] = 1
      dice2[2] = 2
      dice3[2] = 3      

    play_game(player,dice1,pstart.copy(),pscores.copy())
    play_game(player,dice2,pstart.copy(),pscores.copy())
    play_game(player,dice3,pstart.copy(),pscores.copy())
  return


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

play_game(1,[-1,-1,-1],pstart,pscores)

print(wins)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
