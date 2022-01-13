"""
AoC
"""
import time
import sys

start_secs = time.time()

num_elves = 3014603
winner = 1
for i in range(5,num_elves+1):
  winner += 2
  if winner == i:
    winner = -1

print(winner)
# 1834901 too low

end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
