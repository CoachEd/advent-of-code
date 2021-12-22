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

def move_forward(p,n,p1_pos,p2_pos):
  global board_len
  global board

  curr_pos = p1_pos
  if p == 2:
    curr_pos = p2_pos

  end_pos = (curr_pos + n) % 10
  return end_pos

def play_game(player,dice1,dice2,dice3,p1_pos,p2_pos,p1_score,p2_score):
  global wins
  if p1_score >= 21:
    wins[0] += 1
    return
  if p2_score >= 21:
    wins[1] += 1
    return
  
  if dice1 != -1 and dice2 != -1 and dice3 != -1:
    r = dice1 + dice2 + dice3
    spot = move_forward(player,r,p1_pos,p2_pos)
    if player == 1:
      p1_pos = spot
      p1_score += board[spot]
    else:
      p2_pos = spot
      p2_score += board[spot]

    if p1_score >= 21:
      wins[0] += 1
      return
    elif p2_score >= 21:
      wins[1] += 1
      return
    
    dice1 = -1
    dice2 = -1
    dice3 = -1
    # next turn
    if player == 1:
      player = 2
    else:
      player = 1
    play_game(player,dice1,dice2,dice3,p1_pos,p2_pos,p1_score,p2_score)
  else:
    # roll 1, 2, 3
    if dice1 == -1:
      play_game(player,1,dice2,dice3,p1_pos,p2_pos,p1_score,p2_score)
      play_game(player,2,dice2,dice3,p1_pos,p2_pos,p1_score,p2_score)
      play_game(player,3,dice2,dice3,p1_pos,p2_pos,p1_score,p2_score)
    elif dice2 == -1:
      play_game(player,dice1,1,dice3,p1_pos,p2_pos,p1_score,p2_score)
      play_game(player,dice1,2,dice3,p1_pos,p2_pos,p1_score,p2_score)
      play_game(player,dice1,3,dice3,p1_pos,p2_pos,p1_score,p2_score)
    elif dice3 == -1:
      dice3 = 3      
      play_game(player,dice1,dice2,1,p1_pos,p2_pos,p1_score,p2_score)
      play_game(player,dice1,dice2,2,p1_pos,p2_pos,p1_score,p2_score)
      play_game(player,dice1,dice2,3,p1_pos,p2_pos,p1_score,p2_score)
    
    
    
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

play_game(1,-1,-1,-1,pstart[0],pstart[1],pscores[0],pscores[1])

print(wins)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
