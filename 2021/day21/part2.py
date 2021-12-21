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

winners = [0,0]
def quantum_roll(player_turn,pstart,pscores):
  global winners
  global board
  if pscores[0] >= 21:
    winners[0] += 1
    return
  if pscores[1] >= 21:
    winners[1] += 1
    return

  pstart1 = pstart.copy()
  pstart2 = pstart.copy()
  pstart3 = pstart.copy()

  pscores1 = pscores.copy()
  pscores2 = pscores.copy()
  pscores3 = pscores.copy()

  (spot,pstart1) = move_forward(player_turn,1,pstart1)
  pscores1[player_turn-1] += 1

  (spot,pstart2) = move_forward(player_turn,2,pstart2)
  pscores2[player_turn-1] += 2

  (spot,pstart3) = move_forward(player_turn,3,pstart3)
  pscores3[player_turn-1] += 3    

  next_player = -1
  if player_turn == 1:
    next_player = 2
  else:
    next_player = 1
  
  quantum_roll(player_turn,pstart1,pscores1)
  quantum_roll(player_turn,pstart2,pscores2)
  quantum_roll(player_turn,pstart3,pscores3)





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

quantum_roll(1,pstart,pscores)


print(winners)

"""
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
"""



  





print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
