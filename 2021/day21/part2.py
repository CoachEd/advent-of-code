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

def move_forward(p,n):
  global pstart
  global board_len
  global board

  curr_pos = pstart[p-1]
  end_pos = (curr_pos + n) % 10
  pstart[p-1] = end_pos
  return end_pos

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
temp_rolls = 0
r = 0
while True:
  r += roll()
  temp_rolls += 1
  if temp_rolls < 3:
    continue
  
  temp_rolls = 0
  rolls += 3

  spot = move_forward(player,r)
  pscores[player-1] += board[spot]
  if player == 2:
    player = 1
  else:
    player = 2 
  r = 0
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
