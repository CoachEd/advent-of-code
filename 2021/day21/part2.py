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


def quantum_roll(player_turn,pstart,pscores):
  global board
  if pscores[0] >= 21:
    return (1,1) # player 1 wins
  if pscores[1] >= 21:
    return (2,1) # player 2 wins

  ### TODO
  """
  (spot,pstart) = move_forward(player_turn,1,pstart)


  pscores[player_turn-1] += spot


  (spot,pstart) = move_forward(player_turn,2,pstart)
  pscores[player_turn-1] += spot

  (spot,pstart) = move_forward(player_turn,3,pstart)
  pscores[player_turn-1] += spot    

  next_player = -1
  if player_turn == 1:
    next_player = 2
  else:
    next_player = 1
  """
  


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
  return (end_pos,pstart)

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

player = 1
rolls = 0
while True:
  r1 = roll()
  r2 = roll()
  r3 = roll()

  #print('Player ' + str(player) + ': ' + str(r1) + '+'+str(r2) + '+' + str(r3))

  r = r1 + r2 + r3
  rolls += 3
  spot = move_forward(player,r)
  pscores[player-1] += board[spot]
  if player == 2:
    player = 1
  else:
    player = 2  
  if pscores[0] >= 1000 or pscores[1] >= 1000:
    break

# result
if pscores[0] < pscores[1]:
  print(rolls * pscores[0])
else:
  print(rolls * pscores[1])



  





print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
