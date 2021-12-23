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

def move_forward(p,n,positions):
  global board_len
  global board
  return (positions[p-1] + n) % 10

wins = [0,0]
def play_game(player_turn,rolls,positions,scores):

  # execute turn if we can
  if rolls[0] != -1 and rolls[1] != -1 and rolls[2] != -1:
    roll = rolls[0] + rolls[1] + rolls[2]
    spot = move_forward(player_turn,roll,positions)
    scores[player_turn-1] += board[spot]
    if player_turn == 1:
      player_turn = 2
    else:
      player_turn = 1
    rolls[0] = -1
    rolls[1] = -1
    rolls[2] = -1
  
  # winner?
  if scores[0] >= 21:
    wins[0] += 1
    return
  elif scores[1] >= 21:
    wins[1] += 1
    return

  # split universe
  if rolls[0] == -1:
    rolls[0] = 1
    play_game(player_turn,rolls.copy(),positions.copy(),scores.copy())  
    rolls[0] = 2
    play_game(player_turn,rolls.copy(),positions.copy(),scores.copy())  
    rolls[0] = 3
    play_game(player_turn,rolls.copy(),positions.copy(),scores.copy())  
  elif rolls[1] == -1:
    rolls[1] = 1
    play_game(player_turn,rolls.copy(),positions.copy(),scores.copy())  
    rolls[1] = 2
    play_game(player_turn,rolls.copy(),positions.copy(),scores.copy())  
    rolls[1] = 3
    play_game(player_turn,rolls.copy(),positions.copy(),scores.copy())  
  else:
    rolls[2] = 1
    play_game(player_turn,rolls.copy(),positions.copy(),scores.copy())  
    rolls[2] = 2
    play_game(player_turn,rolls.copy(),positions.copy(),scores.copy())  
    rolls[2] = 3
    play_game(player_turn,rolls.copy(),positions.copy(),scores.copy())  


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

play_game(1,[-1,-1,-1],[4,8],[0,0])  

print(wins)
  





print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
